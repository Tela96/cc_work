import csv

linelist = []
txtfile = open('teszt.txt', 'r')
word_dict = {}
for line in txtfile:
    line_p = line.strip('\n')
    linelist = line_p.split(sep=" ")
    for word in linelist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict.update({word: 1})
txtfile.close()
exportfile = open('results.csv', 'w')
writer = csv.writer(exportfile)
writer.writerows(word_dict.items())
exportfile.close()
