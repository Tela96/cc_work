def hypersupersecretmessagerfunction(text):
    secmsg = ""
    for char in text:
        if str.isupper(char):
            secmsg += char
    print(secmsg)


while True:
    text = input('input: ')
    hypersupersecretmessagerfunction(text)
