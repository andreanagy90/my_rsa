def load_public_key():
    with open("public_key.txt", "r") as f:
        lines = f.readlines()
        e = int(lines[-1].strip())

        n = int(lines[-2].strip())
    return e, n



