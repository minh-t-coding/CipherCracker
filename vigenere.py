from constants import Constants
from CipherCrack import freqAnal

def str2num(string):
    nums=[]
    for i in string.lower():
        nums.append(ord(i)-ord('a'))
    return nums

def num2str(nums):
    string=''
    for i in nums:
        string=string+chr(i+ord('a'))
    return string

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def vigenereEncrypt(string,key):
    while len(string)%len(key)!=0:
        string=string+"x"
    nums=[]
    stringNums=str2num(string)
    keyNums=str2num(key)
    for i in range(len(stringNums)):
        nums.append((stringNums[i]+keyNums[i%len(keyNums)])%26)
    return nums

def getKeyLength(string):
    # coincidences[0] is for shift 1
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
        index=0
        characters=[]
        while index<len(string):
            characters.append(string[index])
            index+=keyLength
        freqTable=freqAnal(''.join(characters))
        stringFreqArray=getLetterFreqArray(freqArray)
        
        
            
def getLetterFreqArray(freqArray):
    arr=[]
    for i in range(0,26):
        arr.append(freqArray[chr(i+ord('A'))])
    return arr

def dot(l1,l2):
    assert(len(l1)==len(l2))
    s=0
    for i in range(l1):
        s+=l1[i]*l2[i]
    return s
