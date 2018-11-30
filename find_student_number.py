def printLine(x):
    for i in range(0, x):
        print "=",
    print(" ")

def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False

'''
x[len(x)] overflows array
x[len(x) - 1] equals newline <ENTER>
x[len(x) - 2] is what is desired
'''
def isLastUnknown(x):
    if x[len(x)-2] == "n":
        return True
    else:
        return False
'''
x[len(x)] overflows array
x[len(x) - 1] equals newline <ENTER>
x[len(x) - 2] equals last digit
We check all digits except the last digit
'''
def isOneDigitUnknown(x):
    number_of_ns = 0
    for i in range (0, len(x)-2):
        if x[i] == "n":
            number_of_ns = number_of_ns + 1

    if number_of_ns == 0:
        print("no unknown")
        return False
    elif number_of_ns > 1:
        print("more than 1 unknown")
        return False
    else:
        return True

def getDigit(x):
    printLine(len(x))
    print(x)
    pos_of_n = 0
    for i in range (0, len(x)-2):
        if x[i] == "n":
            pos_of_n = i

    for j in range (0, 10):
        xList = list(x)
        xList[pos_of_n] = str(j)
        x = "".join(xList)
        tSum = 1
        for i in range (0, len(x)-2):
            if isEven(i):
                tSum = tSum + int(x[i])
            else:
                tSum = tSum + 2*int(x[i])
        if tSum%10 == 10 - int(x[len(x)-2]):
            print "n =", j
    return True


'''
len(x) includes newline <ENTER>
len(x) - 1 includes "n"
len(x) - 2 is what is desired
'''
def getLast(x):
    printLine(len(x))
    print(x)
    tSum = 1
    for i in range (0, len(x)-2):
        if isEven(i):
            tSum = tSum + int(x[i])
        else:
            tSum = tSum + 2*int(x[i])

    lastn = 10 - tSum%10
    if lastn == 10:
        lastn = 0

    print "n =", lastn
    return True


mFile = open("student_number_samples.txt", "r")

for line in mFile:
    a = line
    if isLastUnknown(a):
        getLast(a)
    elif isOneDigitUnknown(a):
        getDigit(a)
