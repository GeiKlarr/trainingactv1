numbers = input("Enter a sequence of comma-separated numbers ")
numlist = [int(num) for num in numbers.split(",")] #create loop from numbers and split the numbers to comma
numtuple = tuple(numlist)

print("List: ", numlist)
print("Tuple ", numtuple)