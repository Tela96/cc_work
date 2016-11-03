import csv

def import_inventory(importFile):

    impinv = {}
    row = 0

    file = open(importFile, "r")
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
    print('Inventories merged')
    return mergedinv


def save_inventory(inventory, filename):

    file = open(filename, "w")
    writer = csv.writer(open(filename, 'w'))


    writer.writerows(inventory.items())
    file.close()
    print("Inventory state saved.")


def load_inventory(filename):

    row = 0
    loadinv= {}

    file = open(filename, "r")
    reader = csv.reader(file, quoting = csv.QUOTE_MINIMAL, doublequote = False)

    loadinv=dict((row[0], row[1])for row in reader)

    file.close()
    print("Inventory state loaded.")
    return loadinv
    

