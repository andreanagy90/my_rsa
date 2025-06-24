import math
from p_numbers import generate_prime

def keygen():



    while True:
        p = generate_prime()
        q = generate_prime()
        if q !=p and p > 1000 and q > 1000:
            break
    n = p * q
    z = (p -1) * (q-1)

    e = 65537
    
    if math.gcd(e, z) != 1:
        e = 3
        while math.gcd(e, z) != 1:
            e += 2   
            
    d = pow(e,-1,z)



    with open("public_key.txt", "w") as pub:
        pub.write(f"{n}\n{e}")

    with open ("private_key.txt","w") as priv:
        priv.write(f"{n}\n{d}")

