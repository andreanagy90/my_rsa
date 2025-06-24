import random
from p_numbers import primes_1000, primes_3000, primes_5000
import math

number_list = [primes_1000, primes_3000, primes_5000]



random_list = random.choice(number_list)

p = random.choice(random_list)
q = random.choice(random_list)
n = p * q
z = (p -1) * (q-1)
e = random.randint (1,50000)

if e > n or math.gcd(e,z) > 1:
    e = random.randint (1,10000)


d = random.randint(1,10000000)
if ((e*d)-1 ) % z != 0:
    d = random.randint(1,10000000)

with open("public_key.txt", "w") as pub:
    pub.write(f"{n}\n{e}")

with open ("privat_key.txt","w") as priv:
    priv.write(f"{n}\n{d}")




    

    


