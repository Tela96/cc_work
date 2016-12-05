

def list_handler(in_list):
    max = 0
    min = 100
    for item in in_list:
        if item > max:
            max = item
        if item < min:
            min = item
    result = max - min
    return result


def userinput(text):
    usr_in = input(text)
    return usr_in


def handle_input(text):
    proper_input = False
    while not proper_input:
        try:
            user_input = userinput(text)
            user_input = int(user_input)
            proper_input = True
        except ValueError:
            pass
    return user_input


def list_count():
    text = "How many items do you want in your list? "
    count_list = handle_input(text)
    return count_list


def item_input(count_list):
    counter = 0
    text = "Give one item of the list: "
    usr_list = []
    while counter != count_list:
        list_item = handle_input(text)
        usr_list.append(list_item)
        counter += 1
    return usr_list


def main():
    user_list = []
    usr_list_count = 0
    usr_list_count = list_count()
    user_list = item_input(usr_list_count)
    print(list_handler(user_list))


main()
