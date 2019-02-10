from utils import *
from vigenere import *
from permutation import *


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
print(Constants.englishLetterFreq)

for letter in range(ord('A'),ord('Z')+1):
    let = chr(letter)
    print('Letter:{} Difference:{}'.format(let,freqAnal(ctext)[let]-Constants.englishLetterFreq[let]))

ctext=open('cipher1.txt').read()
plain=shiftBy(ctext,10)
cphr=encryptColTrans(plain.upper(),20)
print(decryptColTrans(cphr)[:40])

