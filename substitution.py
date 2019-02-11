from copy import deepcopy
from utils import *

def substitutionDecrypt(string):
    # initialize cipher
    subcipher={}
    for i in range(0,26):
        letter=chr(i+ord('A'))
        subcipher[letter]=letter
        
    stringFrequencies=freqAnal(string)
    englishLetterFrequencies=deepcopy(Constants.englishLetterFreq)

    strBiFreq = bifreqAnal(string)
    strTopBi = []
    engTopBi = ['th','he','in','er','an','on','st','nt']
    for num in engTopBi:
        strTopBi.append(getMostFrequentLetter(strBiFreq))
        del(strBiFreq[getMostFrequentLetter(strBiFreq)])

    sortedStringFreq = sorted(stringFrequencies.items(), key=lambda kv: kv[1])
    
    i = len(sortedStringFreq)-1
    print("---Monogram Frequencies---")
    for key in Constants.englishLetterFreq:
        print("{}({}) : {}({})".format(key.lower(),englishLetterFrequencies[key],sortedStringFreq[i][0],sortedStringFreq[i][1]))
        i -= 1
    print("---Digram Frequencies---")
    print("Cipher English")
    for i in range(0,len(engTopBi)):
        print("{}\t{}".format(strTopBi[i],engTopBi[i]))

    while len(stringFrequencies)>0:
        mostFreqEng = getMostFrequentLetter(englishLetterFrequencies)
        mostFreqStr = getMostFrequentLetter(stringFrequencies)
        subcipher[mostFreqStr] = mostFreqEng
        del(stringFrequencies[mostFreqStr])
        del(englishLetterFrequencies[mostFreqEng])
    key = ""
    sortedSubCipher = sorted(subcipher.items(), key=lambda kv: kv[1])
    for element in sortedSubCipher:
        key += element[0]
    print("Current proposed key is: {}".format(key))
    key = input("Enter proposed key ('ABCDEFGHIJ...'):")
    print(replaceLetters(string,key))
    ans = input("Does this look correct? ")
    while(ans != "yes"):
        print("Current proposed key is: {}".format(key))
        key = input("Enter proposed key ('ABCDEFGHIJ...'):")
        print("Printing decrypted text...")
        print(replaceLetters(string,key.upper()))
        ans = input("Does this look correct? ")


def substitutionEncrypt(string,cipher):
    ciphertext=[cipher[c] for c in string]
    return ''.join(ciphertext)

def replaceLetters(text, key):
    letterMap = {}
    i = 0
    for letter in range(ord('A'),ord('Z')+1):
        letterMap[key[i]] = chr(letter)
        i += 1
    decryptedStr = []
    for letter in text:
        decryptedStr.append(letterMap[letter])
    return ''.join(decryptedStr)

def getMostFrequentLetter(freqTable):
    maxFrequency=-1
    maxItem=None
    for item in freqTable:
        if freqTable[item]>maxFrequency:
            maxItem=item
            maxFrequency=freqTable[item]
    return maxItem
