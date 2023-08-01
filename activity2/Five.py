def modifyString(word):
    fChar = word[0]
    modifiedString = fChar + word[1:].replace(fChar,"$")
                            #word[1:] slice function
    return modifiedString

print(modifyString("restart"))