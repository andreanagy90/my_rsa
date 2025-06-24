from public import load_public_key


def save_binary(text, filename="binary.txt"):
    bytes_data = text.encode('utf-8')
    binary_list= [format(byte,'08b') for byte in bytes_data]
    binary = "".join(binary_list)
    

    if len(binary) % 8 != 0:
        padding_len = 8 - (len(binary) % 8)
        binary += '0' * padding_len
    else:
        padding_len = 0

    with open ("binary.txt", "w") as f:
        f.write(binary)

    print (f"Your saved binary: {binary}")
    return binary, padding_len


def secret_message(binary_file ="binary.txt"):

    with open (binary_file, "r") as f:
        binary = f.read().strip()

    n, e = load_public_key()

    k_bit = n.bit_length() -1

    padding_len = (k_bit - len(binary) % k_bit) % k_bit  # 0-tól k-1-ig
    binary += "0" * padding_len

    blocks = [binary[i:i+k_bit] for i in range(0, len(binary), k_bit)]

    c_blocks = []

    with open("secret_message_file.txt", "w") as out, open("block_lengths.txt","w") as bl_out:
        for block in blocks:
            m_block = int(block, 2)
            c_block = pow(m_block, e, n)
            c_blocks.append(str(c_block))
            out.write(str(c_block) + "\n")

        bl_out.write(f"{k_bit} {padding_len}\n")

    with open("message_length.txt", "w") as length_file:
        length_file.write(str(len(binary) - padding_len))
        
    return 


def main(text):
    save_binary(text, filename= "binary.txt")

    c_bloks = secret_message("binary.txt")


    return c_bloks