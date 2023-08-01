import datetime


def checkValuesIfSameType(input1,input2):
    if type(input1) and type(input2) == str:
        return input1 + input2
    elif type(input1) and type(input2) == int:
        return input1 * input2
    elif type(input1) and type(input2) == list:
        return list(input1) + list(input2)
    elif type(input1) and type(input2) == dict:
        return dict(input1) , dict(input2)
    elif type(input1) and type(input2) == datetime:
        return input1.days + input2.days
    else:
        return ""




print(checkValuesIfSameType("2023,10,10","2023,10,10"))