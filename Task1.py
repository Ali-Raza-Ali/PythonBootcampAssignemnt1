def strDiag (strInput):
    for i in range(len(strInput)):
        print(' '*i, strInput[i])
stringInput = input("Enter string: ")
strDiag(stringInput)