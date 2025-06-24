from private import load_private_key




def decryption(file="secret_message_file.txt"):
    n, d = load_private_key()
    k = (n.bit_length() + 7) // 8
    k_bit = k * 8
    decrypted_binary = ""

    with open("block_lengths.txt", "r") as bl:
        block_lengths = [line.strip().split() for line in bl.readlines()]
    
    with open(file, "r") as f:
        for i,line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            c_block = int(line)

            m_block = pow(c_block, d, n)

            block_len = int(block_lengths[i][0])
            padding_len = int(block_lengths[i][1])

            block_bin = format(m_block, "b").zfill(block_len)

            if padding_len > 0:
                block_bin[:-padding_len]

            decrypted_binary += block_bin


    print (decrypted_binary)
    return decrypted_binary

def reverse_binary(file="secret_message_file.txt"):

    decrypted_binary = decryption(file)

    while len(decrypted_binary) % 8 != 0:
        decrypted_binary = "0" + decrypted_binary

    text = ""
    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        text += chr(int(byte, 2)) 

    
    print(text)
    return text




