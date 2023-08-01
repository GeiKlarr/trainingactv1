def checkIfEvenOrOdd(num):

    if num % 2==0:
        return "even"
    else:
        return "odd"


while 1>0:

    num = int(input("Enter num: "))
    print(checkIfEvenOrOdd(num))
