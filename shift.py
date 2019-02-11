from utils import *

def shiftBy(ctext, shiftAmt):
    newtext = ""
    for letter in ctext:
        newletter = chr((((ord(letter)-ord('A')) + shiftAmt) % 26) + ord('a'))
        newtext += newletter
    return newtext

def decryptShift(ctext):
    cfreqTable = freqAnal(ctext)
    mostFreq = getMostFrequentLetter(cfreqTable)
    sftAmt = ord('E')-ord(mostFreq)
    if (sftAmt < 0):
        sftAmt += 26
    print("Shift amount: {}".format(sftAmt))
    print(shiftBy(ctext,sftAmt))
