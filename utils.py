class Constants:
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    MAX_VIGENERE_LENGTH = 10

def freqAnal(ctext):
    #returns frequencies of monograms and digrams
    freqTable = {}
    for letter in range(ord('A'),ord('Z')+1):
        freqTable[chr(letter)] = ctext.count(chr(letter))
    #TODO: Digrams??
    return freqTable

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

def dot(l1,l2):
    assert(len(l1)==len(l2))
    s=0
    for i in range(len(l1)):
        s+=l1[i]*l2[i]
    return s        
