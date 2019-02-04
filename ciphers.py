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

def hillEncrypt(string,key):
    while len(string)%len(key)!=0:
        string=string+"x"
    blocks=list(chunkstring(string,len(key)))

    blocknums=[str2num(s) for s in blocks]
    cphrblocks=[]
    for block in blocknums:
        for row in range(len(key)):
            result=0
            for col in range(len(key)):
                result+=key[row][col]*block[col]
            cphrblocks.append(result%26)
    print(cphrblocks)
    return num2str(cphrblocks)
