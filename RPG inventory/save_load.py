import csv


def load_inventory(saveFile):
    impinv = {}
    row = 0
    file = open(saveFile, "r")
    reader = csv.reader(file, quoting = csv.QUOTE_NONE)
    impinv = dict(filter(None, csv.reader(file)))
    #impinv=dict((row[0], row[1])for row in reader)


    print(impinv)
    file.close()