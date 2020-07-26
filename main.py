import hashlib

# def hexa(a, b):
    # return hex(a, b)

print(hex(int("000101", 2)))

def skBinary():
    bin = input("Introduce the binary secret key: ")
    hex = format(int(bin, 2), 'x').upper()
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
            break
        elif sk_type in ["H", "h"]:
            skHex()
            break
        elif sk_type in ["C", "c"]:
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
