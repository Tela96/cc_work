
import sys
if len(sys.argv) < 2 :
    limit = 30
else:
    limit = sys.argv[1]
limit = int(limit)
counter = 0
number1 = 0
number2 = 1
fib = 0
spaces = 0
fiblist = []
#this while helps me get the length of the last number
while counter < limit :
    counter = counter + 1
    fib = number1 + number2
    number1 = number2
    number2 =  fib
    fiblist.append (fib)
#here's where the magic happens    
length = (fiblist[limit-1])
length = str(length)
length = (len(length))
print("Length of last given fibonacci number : ", length)
counter = 0
number1 = 0
number2 = 1
fib = 0
#this while actually lists the (now properly formatted) numbers
while counter < limit :
    counter = counter + 1
    fib = number1 + number2
    number1 = number2
    number2 = fib
    fib = str(fib)
    fiblength = len(fib)
    spaces = (length - fiblength)
    spaces = int(spaces)
    print(" "*spaces, fib, " "*2, "{}.".format(counter))
