def init():
    while True:
        filename = input("Please enter the filename: ")
        if (not filename.endswith(".txt")):
            filename += ".txt"
        
        try:
            ciphertext = open(filename).read()
        except FileNotFoundError:
            print("File not found.")
            continue
        
        return ciphertext
    

def main():
    ciphertext = init()
    print(ciphertext)
    return

main()
