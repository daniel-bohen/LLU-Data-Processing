from pyparsing import condition_as_parse_action
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

options = Options()


def fIDstring(id, driver):
    try:
        _element = driver.find_element(By.ID, id)
    except NoSuchElementException:
        return '-'
    return _element.text

def fLoc(id, driver):
    try:
        myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, id)))
        _element = driver.find_element(By.ID, id)
    except NoSuchElementException:
        return '-'
    states = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 
    'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 
    'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 
    'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 
    'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 
    'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
    'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 
    'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 
    'West Virginia', 'Wisconsin', 'Wyoming']
    check  = _element.text
    for s in states:
        if(s in check):
            return s
    return check


def fClassString(id, driver):
    try:
        _element = driver.find_element(By.CLASS_NAME, id)
    except NoSuchElementException:
        return '-'
    return _element.text


def last(id, driver):
    try:
        _element = driver.find_element(By.CSS_SELECTOR, id)
    except NoSuchElementException:
        return False
    return True

def fdefendant(path, driver):
    try:
        _element = driver.find_elements(By.CLASS_NAME, path)
    except NoSuchElementException:
        return '-'
    if(len(_element) >= 2):
        return _element[1].text
    else:
        return '-'

def fplaintiff(path, driver):
    try:
        _element = driver.find_elements(By.CLASS_NAME, path)
    except NoSuchElementException:
        return '-'
    return _element[0].text

def fsummary(path, driver):
    try:
        _element = driver.find_element(By.ID, path)
    except NoSuchElementException:
        return '-'
    formatted1 = _element.text
    formatted2 = formatted1.replace(",","")
    formatted = formatted2.replace("\n","")
    return formatted

def ver(summary):
    d = ["DENIED", "Denied", "denied", "denies", "DENIES"]
    a = ["Affirm", "Affirmed", 'affirm', "AFFIRM","grants", "GRANTS"]
    e = 'appeal'
    for x in d:
        if((x in summary) and (e not in summary)):
            return x
    for x in a:
        if((x in summary) and (e not in summary)):
            return x
    return "-"

def getCSV(term, searchIndex):
    driver = webdriver.Chrome(options=options, executable_path='/home/danny/career/projects/cdrive/chromedriver')
    driver.get('https://signon.thomsonreuters.com/?productid=CBT&viewproductid=CBTINDIGO&lr=0&culture=en-US')

    of = term + ".csv"
    output = open(of, "a")

    username = 'newTryNow'  # enter your username here
    password = 'WhatOnEarth!'  # enter your password here

    # this code logs into the site
    time.sleep(2)
    u_enter = driver.find_element(By.ID, 'Username').send_keys(username)
    p_enter = driver.find_element(By.ID, 'Password').send_keys(password)
    submit = driver.find_element(By.ID, 'SignIn').click()

    time.sleep(3)
    newSession = driver.find_element(By.ID, 'co_clientIDContinueButton').click()

    time.sleep(4)
    searchTerms = driver.find_element(By.ID, 'searchInputId').send_keys(term)
    search = driver.find_element(By.ID, 'searchButton').click()
    time.sleep(8)

    numResults = driver.find_element(By.CLASS_NAME, 'co_search_titleCount').text
    numResults = numResults[1:]
    numResults = numResults[:-1]
    length = int(numResults.replace(",","")) + 1
    print(numResults)

    firstresult = driver.find_element(By.ID, 'cobalt_result_case_title1').click()
    

    for _ in range(1,length*2):
        time.sleep(2)
        location = fLoc('courtline', driver)
        date = fIDstring('filedate', driver)
        name = fIDstring('title', driver)
        plaintiff = fplaintiff('co_partyLine', driver)
        defendant = fdefendant('co_partyLine', driver)
        summary = fsummary('co_document_0', driver)
        citation = fIDstring('cite0', driver)

        output.write('\n"' + location + '","' + date + '","' + name + '","' + ver(summary) + '","' + plaintiff + '","' + defendant + '","' + citation + '"')

        fName = str(searchIndex) + "/" + str(_) + ".txt"
        sFile = open(fName, "a")
        sFile.write(summary)
        time.sleep(2)
        nextPage = driver.find_element(By.ID, 'co_documentFooterResultsNavigationNext').click()
        index = last("[aria-label='Next Document unavailable']", driver)
        if(index == True):
            break
    
    driver.close()
    

def main():
    getCSV('"pain pump" AND "spine"',1)
    getCSV('"baclofen pump" AND "spine"',2)
    getCSV('"epidural injection" AND "spine"',3)
    getCSV('"facet injection" AND "spine"',4)
    getCSV('"cervical laminoplasty" AND "spine"', 5)
    
    getCSV('"laminectomy" AND "spine"',6)
    getCSV('"anterior lumbar interbody fusion"',7)
    getCSV('"posterior lumbar interbody fusion"',8)
    getCSV('oblique lateral interbody fusion',9)
    getCSV('spinal cord stimulator',10)

    getCSV('"Scoliosis" AND "spine"',11)
    getCSV('"Spine OR spinal" AND "instrumentation"',12)
    getCSV('Dorsal column stimulator',13)
    getCSV('"Bone graft" AND "spine"',14)
    getCSV('Osteotomy',15)

    getCSV('"Anterior cervical discectomy" AND "fusion"',16)
    getCSV('Cervical disc arthroplasty',17)
    getCSV('Posterior cervical foraminotomy',18)
    getCSV('Total disk replacement',19)
    getCSV('Vertebroplasty',20)

    getCSV('Kyphoplasty',21)
    getCSV('"Burst fracture" AND "spine"',22)
    getCSV('"Compression fracture" AND "spine"',23)
    getCSV('"Fracture dislocation" AND "spine"',24)
    getCSV('Dural tear',25)


main()
