import json, csv

def main():
    getCSV('"pain pump" AND "spine"')
    getCSV('"baclofen pump" AND "spine"')
    getCSV('"epidural injection" AND "spine"')
    getCSV('"facet injection" AND "spine"')
    getCSV('"cervical laminoplasty" AND "spine"')
    
    getCSV('"laminectomy" AND "spine"')
    getCSV('"anterior lumbar interbody fusion"')
    getCSV('"posterior lumbar interbody fusion"')
    getCSV('oblique lateral interbody fusion')
    getCSV('spinal cord stimulator')

    getCSV('"Scoliosis" AND "spine"')
    getCSV('"Spine OR spinal" AND "instrumentation"')
    getCSV('Dorsal column stimulator')
    getCSV('"Bone graft" AND "spine"')
    getCSV('Osteotomy')

    getCSV('"Anterior cervical discectomy" AND "fusion"')
    getCSV('Cervical disc arthroplasty')
    getCSV('Posterior cervical foraminotomy')
    getCSV('Total disk replacement')
    getCSV('Vertebroplasty')

    getCSV('Kyphoplasty')
    getCSV('"Burst fracture" AND "spine"')
    getCSV('"Compression fracture" AND "spine"')
    getCSV('"Fracture dislocation" AND "spine"')
    getCSV('Dural tear')


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
