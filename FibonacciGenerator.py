## FibonacciGenerator.py
##
## This program will generate a user-specified amount of fibonacci numbers starting from 1
##
## Aster Fan
##
## June 2017



# State intention of this program
print("\nThis program will print out a Fibonacci sequence of your desired length!")

# Print list sequence (defining variable)
def printSequence():
    print("\nHere is your Fibonacci sequence of %i number(s): \n\t%s" %(length,fibonacciStart))


# Restart Fibonacci sequence list every time we re-run program
x = 1
while x == 1:
    fibonacciStart = [1,1]


# Ask user about the length of desired Fibonacci sequence
    length = int(input("\nEnter your desired Fibonacci sequence length: "))

# Create Fibonacci sequence starting from 1 using maths
    fibonacciStart = [1,1]
    if length <= 0:
        print("The sequence must contain some positive number.")
    if length == 2:
        fibonacciStart = [1,1]
        printSequence()
    if length == 1:
        fibonacciStart = [1]
        printSequence()
    if length >2:
        for i in range(length):
            addNext = int((fibonacciStart[(len(fibonacciStart)- 2)]) + (fibonacciStart[(len(fibonacciStart) - 1)]))
            fibonacciStart.append(addNext)
            if len(fibonacciStart) == length:
                break
        printSequence()
