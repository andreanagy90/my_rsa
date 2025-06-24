import random
from p_numbers import primes_1000, primes_3000, primes_5000
import math
def keygen():
    number_list = [primes_1000, primes_3000, primes_5000]



    random_list = random.choice(number_list)

    p = random.choice(random_list)
    q = random.choice(random_list)

    while q==p:
        q = random.choice(random_list)


    n = p * q
    z = (p -1) * (q-1)

    e = 65537
    
    if math.gcd(e, z) != 1:
        e = 3
        while math.gcd(e, z) != 1:
            e += 2   
    d = 1
    while (e * d) % z != 1:
        d += 1



    with open("public_key.txt", "w") as pub:
        pub.write(f"{n}\n{e}")

    with open ("private_key.txt","w") as priv:
        priv.write(f"{n}\n{d}")




    

    


