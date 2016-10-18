#hello world.py
import sys  
def ifIsTrue():
     print ('Hello', sys.argv[1],'!')

def elseIsTrue():
    print ('Hello World!')
         

def main():
    if (len(sys.argv) > 1):
        ifIsTrue()
    else:
        elseIsTrue()    


main()
