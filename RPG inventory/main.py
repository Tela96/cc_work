global inv
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon meat']
import order
from order import *






def display_inventory(action):
    allItems = 0
    for k, v  in inv.items():
        print(v," ", k)
        if allItems == 0:
            allItems = v
        else:
            allItems = allItems + v
        
    print("total number of items: ", allItems)

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



    
        
    



    '''
    print(type(keyLength))
    print(type(valueLength))
    print(type(a_v_len))
    print(type(a_k_len))
    '''

        #

    #print("longest: ", keyLength)
    
        

    
        






while True:
    action = (input("what do you want to do? : "))
    if action == "C":
        display_inventory(action)
    if action == "A":
        add_to_inventory(inv, dragon_loot)
    elif action == "O":
        
        print_table(inv)
        
