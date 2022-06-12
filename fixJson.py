import json, csv

def main():
    getCSV('epidural injection AND spine') #2923
    # 11/01/2017 - 06/09/2022 935


def getCSV(term):
    f = term+'.json'
    input = open(f)
    data = json.load(input)

    fOut = term + '.csv'
    out = open(fOut, 'w')
    csv_writer = csv.writer(out)
 
    count = 0
    
    for x in data:
        if count == 0:
    
            # Writing headers of CSV file
            header = x.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(x.values())
    
    out.close()

main()