import csv

def load_inventory(saveFile):
    impinv = {}
    row = 0

    file = open(saveFile, "r")
    reader = csv.reader(file, quoting = csv.QUOTE_MINIMAL, doublequote = False)

    next(reader, None)
    impinv=dict((row[0], row[1])for row in reader)

    file.close()

    return impinv


def merge_imported_list(main_inventory, imported_inventory):
    mergedinv = dict(main_inventory)
    importedinv = dict(imported_inventory)

    for k in importedinv.keys():

        if k in mergedinv:
            mergedinv[k] = int(mergedinv[k]) + int(importedinv[k])
        else:
            mergedinv.update({k:importedinv[k]})
    
    return mergedinv
    