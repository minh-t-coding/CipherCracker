from constants import Constants
def numBigrams(stub, remainder):
    bigrNum = 0
    for i in range(0,len(stub)):
        digram = stub[i]+remainder[i]
        if(digram in Constants.englishDigramFreq):
            bigrNum += 1
    return bigrNum

def decryptColTrans(ctext):
    stub = ctext[0:len(ctext)//5]
    remainder = ctext[len(ctext)//5:]
    print(stub)
    print(remainder)
    print(numBigrams(stub,remainder))
