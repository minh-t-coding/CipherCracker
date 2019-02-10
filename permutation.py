from utils import *

def numBigrams(stub, remainder):
    bigrNum = 0
    for i in range(0,len(stub)):
        digram = stub[i]+remainder[i]
        if(digram in Constants.englishDigramFreq):
            bigrNum += 1
    return bigrNum

def encryptColTrans(string,key):
    while len(string)%key>0:
        string=string+'X'
    chunked=list(chunkstring(string,key))
    result=[]
    for i in range(key):
        column=[chunked[j][i] for j in range(len(chunked))]
        result.append(''.join(column))
    return ''.join(result)

def printTransposedCiphertext(cphr,key):
    chunked=list(chunkstring(cphr,len(cphr)//key))
    for i in chunked:
        print(i)

def decryptColTrans(ctext):
    stubsize = Constants.MIN_PERMUTATION_LENGTH
    stub = ctext[:stubsize]
    remainder = ctext[stubsize:]
    maxBigr = numBigrams(stub,remainder)
    numrows = stubsize
    for delta in range(len(remainder)-len(stub)+1):
        if len(ctext)%(stubsize+delta)!=0:
            continue
        #print('delta '+str(delta))
        #print(stub)
        #print(remainder[delta:delta+len(stub)])
        #print(numBigrams(stub,remainder[delta:]))
        bigrNum = numBigrams(stub,remainder[delta:])
        if (bigrNum > maxBigr):
            maxBigr = bigrNum
            numrows = stubsize+delta
    return encryptColTrans(ctext,numrows)

"""
plain=open('justcommonbigrams.txt').read()
cphr=encryptColTrans(plain.upper(),10)
decryptColTrans(cphr)
"""

