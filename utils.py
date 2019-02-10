class Constants:
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    englishDigramFreq = {'TH': 2.71, 'EN': 1.13, 'NG': 0.89, 'HE': 2.33, 'AT': 1.12, 'AL': 0.88,'IN': 2.03, 'ED': 1.08, 'IT': 0.88, 'ER': 1.78, 'ND': 1.07, 'AS': 0.87, 'AN': 1.61, 'TO': 1.07, 'IS': 0.86, 'RE': 1.41, 'OR': 1.06, 'HA': 0.83, 'ES': 1.32, 'EA': 1.00, 'ET': 0.76, 'ON': 1.32, 'TI': 0.99, 'SE': 0.73, 'ST': 1.25, 'AR': 0.98, 'OU': 0.72, 'NT': 1.17, 'TE': 0.98, 'OF': 0.71}
    MAX_VIGENERE_LENGTH = 10
    MIN_PERMUTATION_LENGTH = 17

def freqAnal(ctext):
    #returns frequencies of monograms
    freqTable = {}
    for letter in range(ord('A'),ord('Z')+1):
        freqTable[chr(letter)] = ctext.count(chr(letter))/len(ctext)*100
    return freqTable

def bifreqAnal(ctext):
    freqTable = {}
    for i in range(0,len(ctext)-1):
        digram = "".join([ctext[i],ctext[i+1]])
        if (digram in freqTable):
            freqTable[digram] += 1
        else:
            freqTable[digram] = 1
    return freqTable

def str2num(string):
    nums=[]
    for i in string.upper():
        nums.append(ord(i)-ord('A'))
    return nums

def num2str(nums):
    string=''
    for i in nums:
        string=string+chr(i+ord('A'))
    return string

def dot(l1,l2):
    assert(len(l1)==len(l2))
    s=0
    for i in range(len(l1)):
        s+=l1[i]*l2[i]
    return s

def getLetterFreqArray(freqArray):
    arr=[]
    for i in range(0,26):
        arr.append(freqArray[chr(i+ord('A'))])
    return arr

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
