
from RSA import generatePrime, generateKey, encrypt, decrypt
import codecs
import sys
import binascii

print("Welcome to RSA Messaging System!")
print("****** Client Menu ******")
print("1. Generate Key Pair")
print("2. View Key Pair")
print("3. Encrypt Message")
print("4. Decrypt Message")

print("\n****** Network Menu ******")
print("5. Send Message")
print("6. Receive Messages")

print("\n****** Debug Menu ******")
print("100. Generate Prime")
print("101. Encrypt a Message")


userOption = input("Your Option: ")

if (int(userOption) == 1): 
    generateKey(2048)

if (int(userOption) == 3):
    print("Encryption for: ") 
    print("1. Current Client")
    print("2. Another Client")
    encryptionOption = input("Your Option: ")

    if (encryptionOption == 1):
        userMessage = raw_input("Enter Message to Encrypt: ")
        file = open("n.txt","r")
        n = int(file.read())
        file.close()
        e = 5
        print(encrypt(e,n,userMessage))


    if (encryptionOption == 2):
        userMessage = input("Enter Message to Encrypt: ")
        user_e = input("Enter Public Exponent: ")
        user_n = input("Enter Modulus: ")

if (int(userOption) == 4):
    print("4 for: ") 
    print("1. Current Client")
    print("2. Another Client")
    encryptionOption = input("Your Option: ")

    if (encryptionOption == 1):
        userMessage = raw_input("Enter Ciphertext to Decrypt: ")
        file = open("n.txt","r")
        n = int(file.read())
        file.close()
        file = open("d5.txt","r")
        d5 = int(file.read())
        file.close()
        print(decrypt(n,d5,userMessage))


    if (encryptionOption == 2):
        userMessage = input("Enter Message to Encrypt: ")
        user_e = input("Enter Public Exponent: ")
        user_n = input("Enter Modulus: ")

    


   
    