from utils import *
from vigenere import *
from permutation import *
from substitution import *
from enum import Enum

class Cipher(Enum):
    SHIFT=0
    SUBSTITUTION=1
    PERMUTATION=2
    VIGENERE=3

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

def getCipherType(ctext):
    ic=IC(ctext)
    if (ic<0.075 and ic>0.065):
        freqArray=getLetterFreqArray(freqAnal(ctext))
        englishFreqArray=getLetterFreqArray(Constants.englishLetterFreq)
        for shift in range(26):
            d=dot(englishFreqArray,freqArray[-shift:]+freqArray[:-shift])/len(ctext)
            if d<0.075 and d>0.065:
                if shift==0:
                    return Cipher.PERMUTATION
                else:
                    return Cipher.SHIFT
        return Cipher.SUBSTITUTION
    return Cipher.VIGENERE

ctext = init()
#print(ctext)
cipherType = getCipherType(ctext).name
print(cipherType)
#print(IC(ctext))
#print(freqAnal(ctext))
#print(Constants.englishLetterFreq)
if (cipherType == "SHIFT"):
    decryptShift()
elif (cipherType == "VIGENERE"):
    vigenereDecrypt(ctext)
elif (cipherType == "SUBSTITUTION"):
    substitutionDecrypt(ctext)
elif (cipherType == "PERMUTATION"):
    decryptColTrans(ctext)
else:
    print("This is a one-time pad and cannot be decrypted")

"""
for letter in range(ord('A'),ord('Z')+1):
    let = chr(letter)
    print('Letter:{} Difference:{}'.format(let,freqAnal(ctext)[let]-Constants.englishLetterFreq[let]))

ctext=open('cipher1.txt').read()
plain=shiftBy(ctext,10)
cphr=encryptColTrans(plain.upper(),20)
print(decryptColTrans(cphr)[:40])

"""
