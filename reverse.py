from private import load_private_key


# Definition for decryption
def decryption(file="secret_message_file.txt"):
    n, d = load_private_key()   # load your private keys

    # Open files and check block size (bit) and padding lengths
    with open("block_lengths.txt", "r") as bl_file:
        k_bit, padding_len = map(int, bl_file.readline().strip().split())

    # Check your original message length (no padding)    
    with open("message_length.txt", "r") as length_file:
        message_length = int(length_file.read()) 

    # Initializing the message binary format
    decrypted_binary = ""
    
    # Open secret message's blocks, and decryption
    with open(file, "r") as f:
        for line in f:
            c_block = int(line.strip())          # secret block  - number
            m_block = pow(c_block, d, n)         # RSA ( m = c^d mod n)
            block_bin = format(m_block, "b").zfill(k_bit) # fromat binary, than fill with 0 with k_bit length 
            decrypted_binary += block_bin        # Add to full binary message

    # remove padding
    decrypted_binary = decrypted_binary[:message_length]


    print (f"Your decrypted binari: {decrypted_binary}")
    
    return decrypted_binary
    
# format from binary to character (utf-8)
def reverse_binary(file="secret_message_file.txt"):

    # call decryption function
    decrypted_binary = decryption(file)

    bytes_list = []     # Create a lyst for byte data 

    # cutting 8 bit piece binary text, format decimal
    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        bytes_list.append(int(byte,2))
    
    # list for byte data
    bytes_data = bytes(bytes_list)

    # Try print with UTF-8 decode
    try:
        decoded_text = bytes_data.decode('utf-8')
        return decoded_text
    
    except UnicodeDecodeError:
        print("Nem sikerült UTF-8-ként dekódolni, itt a nyers szöveg:")
        print(bytes_data)
        return bytes_data 

    




