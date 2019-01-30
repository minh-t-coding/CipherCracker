def init():
    filename = input("Please enter the filename: ")
    if (not filename.endswith(".txt")):
        filename += ".txt"
    ciphertext = open(filename).read()
    return ciphertext
    

def main():
    ciphertext = init()
    print(ciphertext)
    return

main()
