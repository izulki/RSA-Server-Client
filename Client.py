
from RSA import generatePrime, generateKey, encrypt, decrypt, sign, verify
import codecs
import sys
import binascii
import requests
import time
import json
import datetime

print("Welcome to RSA Messaging System!")
print("****** Client Menu ******")
print("1. Generate Key Pair")
print("2. Encrypt Message")
print("3. Decrypt Message")
print("4. Sign Message")
print("5. Verify Message")

print("\n****** Network Menu ******")
print("6. Register onto Network")
print("7. Send Message")
print("8. Receive Messages")


print("\n****** Debug Menu ******")
print("100. Generate Prime")
print("101. Encrypt a Message")


userOption = input("Your Option: ")

if (int(userOption) == 1): 
    generateKey(2048)

if (int(userOption) == 2):
    print("Encryption for: ") 
    print("1. This Client")
    print("2. Another Keypair")
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

if (int(userOption) == 3):
    print("Decrypt for: ") 
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

if (int(userOption) == 4):
    userMessage = raw_input("Message to sign: ")
    file = open("n.txt","r")
    modulus = int(file.read())
    file.close()
    file = open("d5.txt","r")
    d5 = int(file.read())
    file.close()
    print(sign(d5, modulus, userMessage))

if (int(userOption) == 5):
    rawMessage = raw_input("Message to verify: ")
    signedMessage = raw_input("Signature to verify: ")
    file = open("n.txt","r")
    modulus = int(file.read())
    file.close()
    print(verify(modulus, 5, signedMessage, rawMessage))

    

if (int(userOption) == 6):
    username = raw_input("Enter Username to Register: ")
    file = open("username.txt","w") 
    file.write(username)
    file.close
    file = open("n.txt","r")
    modulus = file.read()
    file.close()
    getrequest = requests.get('http://142.93.157.193:3000/register/'+username+'/'+modulus)







if (int(userOption) == 7):
    to = raw_input("Enter Recepient: ")
    message = raw_input("Enter Message: ")
    
    # Get Sender Private Exponent (For Signing)
    file = open("d5.txt","r")
    dS = int(file.read())
    file.close()

    # Get Sender Modulus (For Signing)
    file = open("n.txt","r")
    nS = int(file.read())
    file.close()

    # Get Sender Username
    file = open("username.txt","r")
    sender = file.read()
    file.close()

    #Get Recepient Public Key (Modulus)
    recpMod = requests.get('http://142.93.157.193:3000/getmod/'+to)
    nR = recpMod.content #Recepient
    if (nR == "USER NOT FOUND"):
        print("USER NOT FOUND")
    nR = int(nR)
    eR = 5 #Recepient

    #Encrypt message using recepient public key (eR, nR)
    cText = encrypt(5, nR, message)

    #Sign Message using sender private key (dS, nS)
    sText = sign(dS, nS, message)

    msgStruct = {
    "cText": cText,
    "sText": sText,
    "Sender": sender
    }

    timeStr = str(int(time.time()))

    payload = {'json_payload': msgStruct}

    msgJSON = json.dumps(msgStruct)
    sendRequest = requests.get('http://142.93.157.193:3000/send/'+msgJSON+'/'+timeStr+'/'+to)
    print(sendRequest.content)






   





if (int(userOption) == 8):
    #timestamp = raw_input("Enter Time: ") 



    # Get Recepient Username
    file = open("username.txt","r")
    recp = file.read()
    file.close()

    listOfMsgs = requests.get('http://142.93.157.193:3000/recv/list/'+recp)
    json_data = json.loads(listOfMsgs.content)
    print("\n\nYour list of messages: ")
    i = 0
    for title in json_data:
        strip = json_data[i].strip('.json')
        stripInt = int(strip)
        print("MSG [" + str(i) + "] : " + time.ctime(stripInt))
        i = i + 1

    userChoice = raw_input("\nChoose a message to read: ")
    timestamp = json_data[int(userChoice)].strip('.json')
   

    #Get message
    recv = requests.get('http://142.93.157.193:3000/recv/'+timestamp+'/'+recp)
    info = json.loads(recv.content)
    cText = str(info["cText"])
    sender = info["Sender"]
    sText = str(info["sText"])

    # Get Private Key
    file = open("d5.txt","r")
    d = int(file.read())
    file.close()

    file = open("n.txt","r")
    n = int(file.read())
    file.close()

    #Decrypt Message
    pText = decrypt(n, d, cText)

    #Get Sender Public Key (Modulus)
    senderMod = requests.get('http://142.93.157.193:3000/getmod/'+sender)
    nS = senderMod.content #Recepient
    if (nS == "USER NOT FOUND"):
        print("USER NOT FOUND")
    nS = int(nS)
    eS = 5 #Recepient

    #Verify Signature
    print('\n'+time.ctime(int(timestamp)))
    print("--- START MESSAGE ---")
    print(pText)
    print("--- END MESSAGE ---")
    print("SIGNATURE STATUS: ")
    verify(nS, eS, sText, pText)
    print('\n')

