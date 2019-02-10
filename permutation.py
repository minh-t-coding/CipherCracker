from utils import *

def numBigrams(stub, remainder):
    bigrNum = 0
    for i in range(0,len(stub)):
        digram = stub[i]+remainder[i]
        if(digram in Constants.englishDigramFreq):
            bigrNum += 1
    return bigrNum

def decryptColTrans(ctext):
    stub = ctext[0:len(ctext)//7]
    remainder = ctext[len(ctext)//7:]
    print(len(ctext))
    #print(stub)
    #print(len(stub))
    #print(remainder)
    #print(len(remainder))
    #delta = 0
    #print(numBigrams(stub,remainder[delta:]))
    maxBigr = numBigrams(stub,remainder)
    for delta in range(0, len(remainder)-len(stub)):
        print(stub)
        print(remainder[delta:])
        print(numBigrams(stub,remainder[delta:]))
        bigrNum = numBigrams(stub,remainder[delta:])
        if (bigrNum > maxBigr):
            maxBigr = bigrNum
    
