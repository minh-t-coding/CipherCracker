from utils import *


def vigenereEncrypt(string,key):
    while len(string)%len(key)!=0:
        string=string+"X"
    nums=[]
    stringNums=str2num(string)
    keyNums=str2num(key)
    for i in range(len(stringNums)):
        nums.append((stringNums[i]+keyNums[i%len(keyNums)])%26)
    return nums

def getKeyLength(string):
    coincidences=[]
    for shift in range(1,Constants.MAX_VIGENERE_LENGTH+1):
        coincidences.append(0)
        for index in range(shift,len(string)):
            coincidences[-1]+=string[index]==string[index-shift]
    print(coincidences)
    return coincidences.index(max(coincidences))+1

def getKey(string,keyLength):
    englishFreqArray=getLetterFreqArray(Constants.englishLetterFreq)
    keyGuess=[]
    for position in range(keyLength):
        index=position
        characters=[]
        while index<len(string):
            characters.append(string[index])
            index+=keyLength
        freqTable=freqAnal(''.join(characters))
        stringFreqArray=getLetterFreqArray(freqTable)
        
        maxdot=-1
        guessLetter=-1
        for shift in range(26):
            d=dot(englishFreqArray,stringFreqArray[-shift:]+stringFreqArray[:-shift])/len(characters)
            if d>maxdot:
                maxdot=d
                guessLetter=shift
        print(maxdot)
        keyGuess.append(guessLetter)
    return keyGuess
            
def getLetterFreqArray(freqArray):
    arr=[]
    for i in range(0,26):
        arr.append(freqArray[chr(i+ord('A'))])
    return arr


