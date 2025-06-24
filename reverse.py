from private import load_private_key

def decryption(file="secret_message_file.txt"):
    n, d = load_private_key()


    with open("block_lengths.txt", "r") as bl_file:
        k_bit, padding_len = map(int, bl_file.readline().strip().split())

    decrypted_binary = ""
    
    with open(file, "r") as f:
        for line in f:
            c_block = int(line.strip())
            m_block = pow(c_block, d, n)
            block_bin = format(m_block, "b").zfill(k_bit)
            decrypted_binary += block_bin

    if padding_len > 0:
        decrypted_binary = decrypted_binary[:-padding_len]


    print (f"Your decrypted binari: {decrypted_binary}")
    
    return decrypted_binary
    

def reverse_binary(file="secret_message_file.txt"):


    decrypted_binary = decryption(file)

    text = ""
    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        text += chr(int(byte, 2)) 

    try:
        decoded_text = text.encode('latin1').decode('utf-8')
        print(decoded_text)
        return decoded_text
    except UnicodeDecodeError:
        print("Nem sikerült UTF-8-ként dekódolni, itt a nyers szöveg:")
        print(text)
        return text 

    




