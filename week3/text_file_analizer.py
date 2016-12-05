#def word_counter(textfile):


#def sentence_counter(textfile):


#def char_counter(textfile):


def main():
    textfile = open('test.txt', 'r')
    # char_counter(textfile)
    # word_counter(textfile)
    # sentence_counter(textfile)
    counter = 0
    for char in textfile.readline():
        if char != " " or char != "," or char != "." or char != "!" or char != "?" or char != ":":
            counter += 1

    print(counter)


main()
