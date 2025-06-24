from private import load_private_key




def decryption(file="secret_message_file.txt"):
    n, d = load_private_key()

    with open("block_lengths.txt", "r") as bl:
        line = bl.readline().strip()
        block_len, padding_len = map(int, line.split())

    decrypted_binary = ""
    
    with open(file, "r") as f:
        for line in f:
            c_block = int(line)
            m_block = pow(c_block, d, n)
            if not line:
                continue




            block_bin = format(m_block, "b").zfill(block_len)
            decrypted_binary += block_bin

    if padding_len > 0:
        decrypted_binary = decrypted_binary[:-padding_len]




    print (f"Your decrypted binari: {decrypted_binary}")
    print("---- DEBUG ----")
    print(f"Decrypted binary: {decrypted_binary}")
    print(f"Length: {len(decrypted_binary)}")
    print(f"Length % 8: {len(decrypted_binary) % 8}")
    print("----------------")
    
    return decrypted_binary
    

def reverse_binary(file="secret_message_file.txt"):


    decrypted_binary = decryption(file)

    text = ""
    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        text += chr(int(byte, 2)) 

    
    print(text)
    return text




