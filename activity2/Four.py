def calcuInterest(amount,rate,years):
#FV = amount * (1 + rate/100)^years

    fv = amount * (1+(rate/100)) ** years

    return fv

print(calcuInterest(10000,3.5,7))