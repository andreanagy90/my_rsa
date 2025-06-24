import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def generate_prime(limit= 20000):
    attempts = 0
    while True:
        number = random.randint(2, limit)
        attempts += 1
        if is_prime(number):
            print(f"✓ Prím találva {number} ({attempts} próbálkozás után)")
            return number
        if attempts % 1000 == 0:
            print(f"Még mindig keresek... {attempts} próbálkozás")


