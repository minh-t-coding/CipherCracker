def init():
    while True:
        filename = input("Please enter the filename: ")
        if (not filename.endswith(".txt")):
            filename += ".txt"
        
        try:
            ctext = open(filename).read()
        except FileNotFoundError:
            print("File not found.")
            continue
        
        return ctext
    
def IC(ctext):
    #returns the Index of Coincidence
    summation = 0
    N = len(ctext)
    for letter in range(ord('A'),ord('Z')+1):
        ni = ctext.count(chr(letter))
        summation += (ni*(ni-1))
        
    return (summation * (1/(N*(N-1))))

def freqAnal(ctext):
    #returns frequencies of monograms and digrams
    freqTable = {}
    for letter in range(ord('A'),ord('Z')+1):
        freqTable[chr(letter)] = ctext.count(chr(letter))
    #TODO: Digrams??
    return freqTable
    
def main():
    ctext = init()
    print(ctext)
    print(IC(ctext))
    print(freqAnal(ctext))
    return

main()