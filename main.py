from extdata import *
import hashlib
import math
import subprocess
import platform
import random
import time
import bitcoin

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

def base58(address_hex):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    b58_string = ""
    # Get the number of leading zeros
    leading_zeros = len(address_hex) - len(address_hex.lstrip("0"))
    # Convert hex to decimal
    address_int = int(address_hex, 16)
    # Append digits to the start of string
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Add ‘1’ for each 2 leading zeros
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = "1" + b58_string
    return b58_string

def skBinary():
    bin = input("Introduce the binary secret key: ")
    hex = format(int(bin, 2), 'x').upper()
    b58 = bitcoin.hex_to_b58check(hex, magicbyte=128)
    wif = base58(str(b58))
    print(BRed + "PRIVATE INFORMATION (DO NOT SHARE WITH ANYONE):")
    print(BRed + "The binary secret key is:" + Red, bin)
    print(BRed + "The hexadecimal secret key is:" + Red, hex)
    print(BRed + "The B58Check WIF compressed secret key is:" + Red, b58)
    print(BRed + "WIF (public key) is:" + Red, wif)
    quit()

def skHex():
    hex = input("Introduce the hexadecimal secret key: ")

def skB58():
    B58 = input("Introduce the B58Check secret key: ")

# def skRandom():

def inputloop():
    sk_type = input("Please select the input secret key format. [B] for binary, [H] for hexadecimal, [C] for B58Check or [R] if you want to generate a random key: ")
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
    print(Yellow + "Welcome to btcaddress generator! Please consider reading the README.md file before using it for the first time.")
    input("Press Enter to continue..." + Color_Off)
    inputloop()

clear()
time.sleep(0.01)
start()
