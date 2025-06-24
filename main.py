from secret import main
from reverse import reverse_binary


def program():
    message = input("↓↓↓Text your secret message↓↓↓\n")
    main(message)

    decrypted_text = reverse_binary("secret_message_file.txt")
    
    print(f" Your message is: {decrypted_text}")

program()


