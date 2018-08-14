cont = True

def loadArray(thisArray):
        print("loadArray was called")
        
def printArray(thisArray):
    outString = ""
    for num in thisArray:
        outString = outString + str(num) + " "
    print(outString)
    numElements = len(thisArray)
    print('there are {} elements in the array'.format(numElements))

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
theArray = [1,2,3,4,5]
while cont:
    choice = input('Yo add something - L to add numbers to the array; P - print the dummy array; S - sum dat array; X - max of array; N - min of array; Q - quit this crappy program: ')
    if choice == 'l':
        loadArray(theArray)
                
    elif choice == 'p':
        print(theArray)
    elif choice == 's':
        sumArray(theArray)
    elif choice == 'x':
        maxArray(theArray)
    elif choice == 'n':
        minArray(theArray)
    elif choice == 'q':
        cont = False
          