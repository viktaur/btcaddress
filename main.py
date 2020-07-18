import hashlib

def start():
    print("Welcome to btcaddress generator! Please consider reading the README.md file before using it for the first time.")
    input("Press Enter to continue...")
    sk_type = input("Please select the private key format. [B] for binary, [H] for hexadecimal or [C] for B58Check")
    if sk_type in ["B", "b"]:
        skBinary()
    elif sk_type in ["H", "h"]:
        skHex()
    elif sk_type in ["C", "c"]:
        skB58()
    else:
        print("Please try again")
