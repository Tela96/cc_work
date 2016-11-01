import csv

def load_inventory(saveFile):
    impinv = {}
    row = 0
    file = open(saveFile, "r")
    reader = csv.reader(file, quoting = csv.QUOTE_MINIMAL, doublequote = False)
    next(reader, None)
    #impinv = dict(filter(None, csv.reader(file, quoting = csv.QUOTE_NONE)))
    impinv=dict((row[0], row[1])for row in reader)
    for k, v in impinv.items():
        print(v, " ", k)
    file.close()
    return impinv


def merge_imported_list(main_inventory, imported_inventory):
    mergedinv = dict(main_inventory)
    importedinv = dict(imported_inventory)

    for k in mergedinv.keys():
        if k in importedinv:
            mergedinv[k] = int(mergedinv[k]) + int(importedinv[k])
        else:
            mergedinv.update({k:importedinv[k]})
    
    print(mergedinv)
    return mergedinv
    