def testNum100(num):

    if(num % 100 ==0):
        print(str(num), " = ", end="")
        return True
    else:
        return False


while 1>0:
    num = int(input("Enter number to check "))
    print(testNum100(num))