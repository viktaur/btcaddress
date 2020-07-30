from extdata import *
import hashlib
import math
import subprocess
import platform
import random
import time
import bitcoin
import argparse

from binascii import hexlify, unhexlify
from struct import Struct
from utils import g, b58encode, b58decode


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

def wif_to_key(wif):
    slicer = 4
    if wif[0] in ['K', 'L']:
        slicer = 5

    return hexlify(b58decode(wif)[1:-slicer]).decode('utf-8')

def skBinary():
    bin = input("Introduce the binary secret key: ")
    hex = format(int(bin, 2), 'x').upper()
    b58 = bitcoin.hex_to_b58check(hex, magicbyte=128)
    pub_key = wif_to_key(b58)
    print(BRed + "PRIVATE INFORMATION (DO NOT SHARE WITH ANYONE):")
    print(BRed + "The binary secret key is:" + Red, bin)
    print(BRed + "The hexadecimal secret key is:" + Red, hex)
    print(BRed + "The B58Check WIF compressed secret key is:" + Red, b58)
    print(BGreen + "PUBLIC INFORMATION (SAFE TO SHARE)")
    print(BGreen + "WIF (public key) is:" + Green, pub_key)
    quit()

def skHex():
    hex = input("Introduce the hexadecimal secret key: ")
    bin = bin(int(hex, 16))[2:]
    b58 = bitcoin.hex_to_b58check(hex, magicbyte=128)
    # pub_wif = base58(b58)
    print(BRed + "PRIVATE INFORMATION (DO NOT SHARE WITH ANYONE):")
    print(BRed + "The binary secret key is:" + Red, bin)
    print(BRed + "The hexadecimal secret key is:" + Red, hex)
    print(BRed + "The B58Check WIF compressed secret key is:" + Red, b58)
    # print(BRed + "WIF (public key) is:" + Red, pub_wif)
    quit()

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
