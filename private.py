def load_private_key():
    with open("private_key.txt", "r") as f:
        lines = f.readlines()
        d = int(lines[-1].strip())

        n = int(lines[-2].strip())
    return n, d




