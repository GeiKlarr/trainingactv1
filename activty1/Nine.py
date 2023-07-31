def calcuN(n):
    nstr = str(n)

    nn = nstr + nstr

    nnn = nstr + nstr + nstr

    result = n + int(nn) + int(nnn)

    return result

num = int(input("Enter integer: "))
print(calcuN(num))