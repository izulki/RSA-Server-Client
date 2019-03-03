
from RSA import generatePrime, generateKey

print("Welcome to RSA Messaging System!")
print("****** Main Menu ******")
print("1. Generate Key Pair")
print("2. View Key Pair")
print("3. Send Message")
print("4. Receive Messages")

print("****** Debug Menu ******")
print("100. Generate Prime")


userOption = input("Your Option: ")

if (userOption == 1): 
    generateKey(2048)

if (userOption == 100):
    print(generatePrime(1024))