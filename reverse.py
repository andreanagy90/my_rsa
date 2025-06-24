from private import load_private_key

def decryption(file="secret_message_file.txt"):
    n, d = load_private_key()


    with open("block_lengths.txt", "r") as bl_file:
        k_bit, padding_len = map(int, bl_file.readline().strip().split())
    
    with open("message_length.txt", "r") as length_file:
        message_length = int(length_file.read()) 

    decrypted_binary = ""
    
    with open(file, "r") as f:
        for line in f:
            c_block = int(line.strip())
            m_block = pow(c_block, d, n)
            block_bin = format(m_block, "b").zfill(k_bit)
            decrypted_binary += block_bin

    decrypted_binary = decrypted_binary[:message_length]


    print (f"Your decrypted binari: {decrypted_binary}")
    
    return decrypted_binary
    

def reverse_binary(file="secret_message_file.txt"):


    decrypted_binary = decryption(file)

    bytes_list = []

    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        bytes_list.append(int(byte,2))
    
    bytes_data = bytes(bytes_list)

    try:
        decoded_text = bytes_data.decode('utf-8')
        return decoded_text
    
    except UnicodeDecodeError:
        print("Nem sikerült UTF-8-ként dekódolni, itt a nyers szöveg:")
        print(bytes_data)
        return bytes_data 

    




