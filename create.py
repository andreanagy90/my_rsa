import math
#from p_numbers import generate_prime
from Crypto.Util.number import getPrime, inverse        # import Crypto functions

# generate public and private keys

def keygen(keysize= 2048):




    p = getPrime(keysize//2)
    q = getPrime(keysize//2)
    while p == q:
        q = getPrime(keysize//2)

    n = p * q
    z = (p -1) * (q-1)

    e = 65537
    
    if math.gcd(e, z) != 1:
        raise ValueError ("e and z no relative prime, generate again")
            
    d = inverse(e,z)



    with open("public_key.txt", "w") as pub:
        pub.write(f"{n}\n{e}")

    with open ("private_key.txt","w") as priv:
        priv.write(f"{n}\n{d}")

    return (n, e), (n, d)

