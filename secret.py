from public import load_public_key


# format your message to 8 bit binary data
def save_binary(text, filename="binary.txt"):
    bytes_data = text.encode('utf-8')       # Format to UTF-8
    binary_list= [format(byte,'08b') for byte in bytes_data]    # Transform byte to 8 bit binary data, and save
    binary = "".join(binary_list)    # # Binary datas to 1 character string
    
    # if binary length % 8 != 0, add "0" to padding
    if len(binary) % 8 != 0:
        padding_len = 8 - (len(binary) % 8) # missing bits len
        binary += '0' * padding_len         # add 0
    else:
        padding_len = 0                     # no padding

    # save to file
    with open ("binary.txt", "w") as f:
        f.write(binary)

    print (f"Your saved binary: {binary}")

    # return to value
    return binary, padding_len


# Binary string encryption
def secret_message(binary_file ="binary.txt"):

    # open and read binary datas
    with open (binary_file, "r") as f:
        binary = f.read().strip()

    n, e = load_public_key()        # Load public keys n, e

    k_bit = n.bit_length() -1       # max block size bit ( < n )

    # if binary data % k_bit blocks != 0 --- add 0 to end
    padding_len = (k_bit - len(binary) % k_bit) % k_bit  # from 0 - to k-1
    binary += "0" * padding_len

    # Division to k_bit blocks
    blocks = [binary[i:i+k_bit] for i in range(0, len(binary), k_bit)]

    # encrypted blocks 
    c_blocks = []

    # save blocks
    with open("secret_message_file.txt", "w") as out, open("block_lengths.txt","w") as bl_out:
        for block in blocks:
            m_block = int(block, 2)         # binary to number
            c_block = pow(m_block, e, n)    # RSA : c = m^e mod n
            c_blocks.append(str(c_block))   # add to list   
            out.write(str(c_block) + "\n")  # write to file

        bl_out.write(f"{k_bit} {padding_len}\n")    # write padding len and binary len

    # save binary length without padding
    with open("message_length.txt", "w") as length_file:
        length_file.write(str(len(binary) - padding_len))

    # no value        
    return 

# main program
def main(text):
    save_binary(text, filename= "binary.txt")   # call save binary function

    c_bloks = secret_message("binary.txt")      # call secret message function as c_blocks


    return c_bloks                              # return to value