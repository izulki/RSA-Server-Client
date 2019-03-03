
from RSA import generatePrime, generateKey
import codecs
import sys
import binascii

print("Welcome to RSA Messaging System!")
print("****** Main Menu ******")
print("1. Generate Key Pair")
print("2. View Key Pair")
print("3. Send Message")
print("4. Receive Messages")

print("****** Debug Menu ******")
print("100. Generate Prime")
print("101. Encrypt a Message")


userOption = input("Your Option: ")

if (int(userOption) == 1): 
    generateKey(2048)

if (userOption == 100):
    print(generatePrime(1024))

if (userOption == 101):
    ###### SHOULD GET PUBLIC KEY HERE ######
    ## GET ANOTHER CLIENT  n ####
    file = open("n.txt","r")
    n = int(file.read())
    file.close

    ### GET ANOTHER CLIENT e ###
    e = 5
    
    userMsg_str = raw_input("Enter a message: ")
    userMsg_intArr = [(ord(c)) for c in userMsg_str] #list compression, convert each character to unicode (Decimal)
    print(userMsg_intArr)
    userMsg_hexStr = "0x" + binascii.hexlify(bytearray(userMsg_intArr))
    print(userMsg_hexStr)
    userMsg_bigInt = int(userMsg_hexStr, 16)
    print(userMsg_bigInt)
    userMsg_ctext =  pow(userMsg_bigInt, e, n)
    print(userMsg_ctext)

    # Testing for Decreyption
    file = open("d5.txt","r")
    d5 = int(file.read())
    file.close

    ptext = pow(userMsg_ctext, d5, n)
    print(ptext)
    decode_hexStrRaw = hex(ptext) #string
    print(decode_hexStrRaw)
    decode_hexStr = decode_hexStrRaw[2:-1]
    print(decode_hexStr)

    msg = bytearray.fromhex(decode_hexStr)
    print(msg)


    


   
    