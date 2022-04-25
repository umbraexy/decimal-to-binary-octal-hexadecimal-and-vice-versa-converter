#!/usr/bin/python3

number= ""

number = input("Enter number you want to convert: \n")

base= ""

base = input("Enter current number's current base. \n  b-binary,b-octal,d-decimal,x-hexadecimal \n")

dformat=""
while (not(dformat == "b" or dformat=="o" or dformat=="d" or dformat=="h")):
    
    dformat = input("Enter desired format.\n You should use the character format: \n b (binary), o (octal), d (decimal), h (hexadecimal) \n")

intbase= 0;
if base=="o":
    intbase=8
elif base=="b":
    intbase=2;
elif base=="d":
    intbase=10;
elif base=="x":
    intbase=16;

if dformat == "o":
    octalstring = oct(int(number))
    print(octalstring[2:(len(octalstring))])

elif dformat == "b":
    binarystring = bin(int(number))
    print(binarystring[2:(len(binarystring))])

elif dformat == "h":
    hexastring = hex(int(number))
    print(hexastring[2:(len(hexastring))])

elif dformat == "d":
    decimalstring = int(("0"+base+number),intbase)
    print(decimalstring)


    
