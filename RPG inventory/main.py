inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon meat']





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
    ni = dragon_loot
    for k in dragon_loot:
        if k in inv:
            inv[k] +=1
        else:
            inv.update({k:1})
       
def print_table():

    keyLength = 0
    valueLength = 0

    for k, v in inv.items():

        if valueLength < len(str(v)):
            valueLength = len(str(v))

        if keyLength < len(str(k)):
            keyLength = len(str(k))

    keyLength = int(keyLength)
    

    for k, v in inv.items():

        a_v_len = (int(len(str(v))))
        a_k_len = (int(len(str(k))))

        frontspaces=(valueLength-a_v_len)
        spaces=(keyLength-a_k_len)
        dashes = valueLength + keyLength + spaces + frontspaces + 10 + 5
        print(" "*10 ," "*frontspaces, v," "*5, " "*spaces, k)
        
    



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
        print_table()
        
