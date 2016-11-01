import csv

def load_inventory(saveFile):
    impinv = {}
    row = 0
    file = open(saveFile, "r")
    reader = csv.reader(file, quoting = csv.QUOTE_MINIMAL, doublequote = False)
    #impinv = dict(filter(None, csv.reader(file, quoting = csv.QUOTE_NONE)))
    impinv=dict((row[0], row[1])for row in reader)
    for k, v in impinv.items():
        print(v, " ", k)
    file.close()