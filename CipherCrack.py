from utils import *
from vigenere import *

def init():
    while True:
        filename = input("Please enter the filename: ")
        if (not filename.endswith(".txt")):
            filename += ".txt"
        
        try:
            ctext = open(filename).read()
        except FileNotFoundError:
            print("File not found.")
            continue
        
        return ctext
    
def IC(ctext):
    #returns the Index of Coincidence
    summation = 0
    N = len(ctext)
    for letter in range(ord('A'),ord('Z')+1):
        ni = ctext.count(chr(letter))
        summation += (ni*(ni-1))
        
    return (summation * (1/(N*(N-1))))


def shiftBy(ctext, shiftAmt):
    newtext = ""
    for letter in ctext:
        newletter = chr((((ord(letter)-ord('A')) + shiftAmt) % 26) + ord('a'))
        newtext += newletter
    return newtext



ctext = init()
print(ctext)
print(IC(ctext))
print(freqAnal(ctext))
print(getKey(ctext,1))
print(shiftBy(ctext,10))
print(Constants.englishLetterFreq)
print(getKeyLength(ctext))

print(vigenereDecrypt(ctext))
"""
vtest=shiftBy(ctext,10)
ctext=vigenereEncrypt(vtest,'fuck')
keyLen=getKeyLength(ctext)
print(keyLen)
print((getKey(ctext,keyLen)))
print(vigenereEncrypt(ctext,num2str(getKey(ctext,keyLen))))
"""
