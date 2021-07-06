"""
Project: Decimal to Binary Converter
Purpose: This program will convert a Decimal IPv4 address into its Binary version
Created by: Josh Thrash
Date: February 26, 2021
"""




inputIP = input("Enter your IPv4 Address: ")
inputList = inputIP.split(".")
inputListInt = [int(i) for i in inputList]
OctetOneString = []

#This function takes the first three octets when called and calculates what the binary value is while adding a decimal
def BinaryFormula(Octet_0):
    NoAppend(Octet_0)
    OctetOneString.append(".")
    return OctetOneString

#This function performs the same for the last octet but does not add decimal point to end
def NoAppend(Octet_0):

    try:
        if Octet_0 >= 128 and Octet_0 < 256:
            OctetOneString.append(1)
            Octet_1 = int(Octet_0 - 128)
        elif Octet_0 < 128:
            OctetOneString.append(0)
            Octet_1 = Octet_0

        if Octet_1 >= 64:
            OctetOneString.append(1)
            Octet_2 = Octet_1 - 64
        elif Octet_1 < 64:
            OctetOneString.append(0)
            Octet_2 = Octet_1

        if Octet_2 >= 32:
            OctetOneString.append(1)
            Octet_3 = Octet_2 - 32
        elif Octet_2 < 32:
            OctetOneString.append(0)
            Octet_3 = Octet_2

        if Octet_3 >= 16:
            OctetOneString.append(1)
            Octet_4 = Octet_3 - 16
        elif Octet_3 < 16:
            OctetOneString.append(0)
            Octet_4 = Octet_3

        if Octet_4 >= 8:
            OctetOneString.append(1)
            Octet_5 = Octet_4 - 8
        elif Octet_4 < 8:
            OctetOneString.append(0)
            Octet_5 = Octet_4

        if Octet_5 >= 4:
            OctetOneString.append(1)
            Octet_6 = Octet_5 - 4
        elif Octet_5 < 4:
            OctetOneString.append(0)
            Octet_6 = Octet_5

        if Octet_6 >= 2:
            OctetOneString.append(1)
            Octet_7 = Octet_6 - 2
        elif Octet_6 < 2:
            OctetOneString.append(0)
            Octet_7 = Octet_6

        if Octet_7 >= 1:
            OctetOneString.append(1)
        else:
            OctetOneString.append(0)
    except IndexError:
        print("Please enter a digit followed by a period for each octet")
    else:
        return OctetOneString


#This loop creates the binary form from the conversion formula
def OctetLoop(var):
    index = var
    for i in var:
        print(i, end = "")

#These variables hold the returns from the Conversion Formulas Function
OctetBinary1 = BinaryFormula(inputListInt[0])
OctetBinary2 = BinaryFormula(inputListInt[1])
OctetBinary3 = BinaryFormula(inputListInt[2])
OctetBinary4 = NoAppend(inputListInt[3])

