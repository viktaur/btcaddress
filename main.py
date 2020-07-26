import hashlib
import math

def skBinary():
    bin = input("Introduce the binary secret key: ")
    hex = format(int(bin, 2), 'x').upper()

    print("DO NOT SHARE WITH ANYONE")
    print("The binary secret key is:", bin)
    print("The hexadecimal secret key is:", hex)

def skHex():
    hex = input("Introduce the hexadecimal secret key: ")

def skB58():
    B58 = input("Introduce the B58Check secret key: ")

def skRandom():

def inputloop():
    sk_type = input("Please select the input secret key format. [B] for binary, [H] for hexadecimal, [C] for B58Check or [R] if you want to generate a random key")
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
        elif sk_type in ["R", "r"]:
            skRandom()
        else:
            print("Please try again")
            inputloop()

def start():
    print("Welcome to btcaddress generator! Please consider reading the README.md file before using it for the first time.")
    input("Press Enter to continue...")
    inputloop()


start()
