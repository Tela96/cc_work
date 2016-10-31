inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}





def display_inventory(action):
    if action == "y":
        print(inv)






while True:
   action = (input("do you want to check your inventory?: "))
