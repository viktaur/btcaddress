import hashlib

# loop = True

def skBinary():
    bin = str(input("Introduce the binary secret key: "))
    hex = hex(int(bin, 2))
    print(hex)

def skHex():
    inputHex = input("Introduce the hexadecimal secret key: ")

def skB58():
    inputB58 = input("Introduce the B58Check secret key: ")

def inputloop():
    sk_type = input("Please select the secret key format. [B] for binary, [H] for hexadecimal or [C] for B58Check: ")
    while True:
        if sk_type in ["B", "b"]:
            skBinary()
        elif sk_type in ["H", "h"]:
            skHex()
        elif sk_type in ["C", "c"]:
            skB58()
        else:
            print("Please try again")
            inputloop()

def start():
    print("Welcome to btcaddress generator! Please consider reading the README.md file before using it for the first time.")
    input("Press Enter to continue...")
    inputloop()


start()
