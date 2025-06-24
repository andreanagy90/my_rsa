from public import load_public_key


def save_binary(text, filename="binary.txt"):
    binary_list= [format(ord(char),'08b') for char in text]
    binary = "".join(binary_list)
    with open ("binary.txt", "w") as f:
        f.write(binary)
    print (f"Your saved binary: {binary}")
    return binary


def secret_message(binary_file ="binary.txt"):

    with open (binary_file, "r") as f:
        binary = f.read().strip()

    n, e = load_public_key()

    k = (n.bit_length() +7) // 8
    k_bit = k * 8

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
    return c_blocks


def main(text):
    save_binary(text, filename= "binary.txt")

    c_bloks = secret_message("binary.txt")


    return c_bloks