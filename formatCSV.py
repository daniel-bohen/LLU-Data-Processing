import os
import re

def getCSV(term, folder, total):

    global dollar
    

    total = total + 1
    script_dir = os.path.dirname(__file__)
    fileName = term + '.csv'
    c = open(fileName, 'r')

    # ofName = "WL_" + term + '.csv'
    # o = open(ofName, "w")

    lines = c.readlines()
    _ = 1
    for line in lines:
        filePath = script_dir + '/' + str(folder) + '/' + str(_) + '.txt'
        f = open(filePath, 'r')

        output = f.read()
        numD = output.count('$')
        dollar += numD
       
        output = re.sub(r'[^a-zA-Z.: ()0-9-*—\/]','',output)
        line = line.replace('\n','')

        output = ',"' + output + '",\n'

        output = line + output

        # o.write(output)

        f.close()

        _ += 1

    print(dollar)
    c.close()







def main():
    global dollar
    dollar = 0

    getCSV('"pain pump" AND "spine"',1, 63)
    getCSV('"baclofen pump" AND "spine"',2, 20)
    getCSV('"epidural injection" AND "spine"',3, 2808)
    getCSV('"facet injection" AND "spine"',4, 690)
    getCSV('"cervical laminoplasty" AND "spine"', 5, 21)
    
    getCSV('"laminectomy" AND "spine"',6, 3132)
    getCSV('"anterior lumbar interbody fusion"',7, 218)
    getCSV('"posterior lumbar interbody fusion"',8, 235)
    getCSV('oblique lateral interbody fusion',9, 19)
    getCSV('spinal cord stimulator',10, 1383)

    getCSV('"Scoliosis" AND "spine"',11, 4975)
    getCSV('"Spine OR spinal" AND "instrumentation"', 12, 27)
    getCSV('Dorsal column stimulator',13, 174)
    getCSV('"Bone graft" AND "spine"',14, 583)
    getCSV('Osteotomy',15, 585)

    getCSV('"Anterior cervical discectomy" AND "fusion"',16, 1168)
    getCSV('Cervical disc arthroplasty',17, 199)
    getCSV('Posterior cervical foraminotomy',18, 98)
    getCSV('Total disk replacement',19, 697)
    getCSV('Vertebroplasty',20, 54)

    getCSV('Kyphoplasty',21, 105)
    getCSV('"Burst fracture" AND "spine"',22, 124)
    getCSV('"Compression fracture" AND "spine"',23, 2042)
    getCSV('"Fracture dislocation" AND "spine"',24, 729)
    getCSV('Dural tear',25, 69)


main()