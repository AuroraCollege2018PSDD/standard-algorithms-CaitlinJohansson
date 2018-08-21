cont = True

def loadArray(thisArray):
        theArray.append(numbs)
        print(theArray)
        #append an array python
        
def printArray(thisArray):
    outString = ""
    for num in thisArray:
        outString = outString + str(num) + " "
    print(outString)
    numElements = len(thisArray)
    print('There are {} elements in the array'.format(numElements))

def sumArray(thisArray):
    sum = 0
    for num in thisArray:
        sum = sum + num
    print(sum)
    
def maxArray(thisArray):
    print('maxArray was called')

def minArray(thisArray):
    print('minArray was called')
    

#main program
theArray = []
while cont:
    choice = input('Yo add something - L to add numbers to the array; P - print the dummy array; S - sum dat array; X - max of array; N - min of array; Q - quit this crappy program: ')
    if choice == 'l':
        try:
            numbs = int(input('Enter a number of your choice to put into the array: '))
        except ValueError:
          print("That's not an int!")
        else:
            loadArray(theArray)
    elif choice == 'p':
        printArray(theArray)
    elif choice == 's':
        sumArray(theArray)
    elif choice == 'x':
        maxArray(theArray)
    elif choice == 'n':
        minArray(theArray)
    elif choice == 'q':
        cont = False
          