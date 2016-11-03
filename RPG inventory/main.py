import order
from order import *
import save_load
from save_load import *


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon meat']
def allitems(inventory):
    
    allItems = 0
    for k, v in inv.items():
        if allItems == 0:
            allItems = v

        else:
            allItems = allItems + v
    
    print("total number of items: ", allItems)

def display_inventory(action):


    for k, v  in inv.items():
        print(v," ", k)
    
    allitems(inv)



def add_to_inventory(inventory,added_items):

    for k in dragon_loot:

        if k in inv:
            inv[k] +=1

        else:
            inv.update({k:1})

       
def print_table(inventory):

    sorting = input(str("how would you like your inventory? "))

    if sorting == "Desc":
        order_sorted(inv)

    elif sorting == "Asc":
        order_reversed(inv)

    else:
        order_default(inv)


while True:

    action = (input("what do you want to do? : "))

    if action == "C":
        display_inventory(action)

    elif action == "A":
        add_to_inventory(inv, dragon_loot)

    elif action == "O":
        print_table(inv)
        allitems(inv)

    elif action == "I":
        impinv ={}
        impinv = import_inventory('import_inventory.csv')
        inv = merge_imported_list(inv, impinv)

    elif action == "S":
        save_inventory(inv, 'Savegame.csv')

    elif action == "L":
        inv = load_inventory('Savegame.csv')
    elif action == "Q":
        quit()