inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']





def display_inventory(action):
    for k, v  in inv.items():
        print(v," ", k)

def add_to_inventory(inventory,added_items):
    ni = dragon_loot
    for i in dragon_loot:
        if KeyError:
            inv[i] += 1
        else:
            inv.update({i:1})
       
        

    
        






while True:
    action = "A" #(input("what do you want to do? : "))
    #if action == "C":
     #   display_inventory(action)
    if action == "A":
        add_to_inventory(inv, dragon_loot)
    elif action == "t":
        print(inv['gold coin'])
