import hashlib

def skB58():

def skHex():
    format(hex)

def skBinary():
    print("Binary secret key:", bin)
    print(hex)

def inputloop():
    sk_type = input("Please select the secret key format. [B] for binary, [H] for hexadecimal or [C] for B58Check: ")
    while True:
        if sk_type in ["B", "b"]:
            bin = input("Introduce the binary secret key: ")
            hex = format(int(bin, 2), 'x').upper()
            skBinary()
            break
        elif sk_type in ["H", "h"]:
            hex = input("Introduce the hexadecimal secret key: ")
            skHex()
            break
        elif sk_type in ["C", "c"]:
            B58 = input("Introduce the B58Check secret key: ")
            skB58()
            break
        else:
            print("Please try again")
            inputloop()

def start():
    print("Welcome to btcaddress generator! Please consider reading the README.md file before using it for the first time.")
    input("Press Enter to continue...")
    inputloop()


start()
