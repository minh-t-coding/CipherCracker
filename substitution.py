from copy import deepcopy
from utils import *

def substitutionDecrypt(string):
    # initialize cipher
    subcipher={}
    for i in range(0,26):
        letter=chr(i+ord('A'))
        subcipher[letter]=letter
    englishLetterFrequencies=copy.

def substitutionEncrypt(string,cipher):
    ciphertext=[cipher[c] for c in string]
    return ''.join(ciphertext)

def getMostFrequentLetter(freqTable):
    maxFrequency=-1
    maxItem=None
    for item in freqTable:
        if freqTable[item]>maxFrequency:
            maxItem=item
            maxFrequency=freqTable[item]
    return maxItem
