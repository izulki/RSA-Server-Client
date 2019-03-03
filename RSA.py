from fractions import gcd
from random import getrandbits, randrange
from RM import isPrime, rabinMiller
from RSAMath import egcd, modinv

#GeneratePrime (RSA) 
def generatePrime(primeSize): #size of prime in bits 
    if (primeSize >= 1024) and (primeSize <= 4096):
        maxAttempt = 100 * primeSize
        while maxAttempt:
            maxAttempt = maxAttempt - 1
            potPrime = randrange(2**(primeSize-1), (2**primeSize)-1)
            if (potPrime%3 != 1) and (potPrime%5 != 1) and (isPrime(potPrime)): #Note: IsPrime and rabinMiller Imported
                return potPrime
            else:
                pass

### RSA Functions ###
def generateKey(modSize):
    p = 0
    q = 0
    n = 0
    d3 = 0
    d5 = 0
    if(modSize >= 2048) and (modSize <= 8192):
        p = generatePrime(modSize/2)
        q = generatePrime(modSize/2)
        if(p != q):
            #t = lcm(p,q)
            t = ((p-1)*(q-1))/gcd(p-1,q-1)
            g, u, v = egcd(3, t) #Note: EGCD Function Imported
            assert (g == 1)
            d3 = u%t

            g, u, v = egcd(5, t)
            assert (g == 1)
            d5 = u%t

            n = p*q

            print("--- Large Prime: p ---")
            print(p)
            file = open("p.txt","w") 
            file.write(str(p))
            file.close

            print("\n--- Large Prime: q ---")
            print(q)
            file = open("q.txt","w") 
            file.write(str(q))
            file.close

            print("\n--- Modulus: n ---")
            print(n)
            file = open("n.txt","w") 
            file.write(str(n))
            file.close

            print("\n--- Private Signing Exponent: d3 ---")
            print(d3)
            file = open("d3.txt","w") 
            file.write(str(d3))
            file.close

            print("\n--- Private Decryption Exponent: d5 ---")
            print(d5)
            file = open("d5.txt","w") 
            file.write(str(d5))
            file.close




