from secret import main
from reverse import reverse_binary


def program():
    message = input("↓↓↓Text your secret message↓↓↓\n")
    main(message)

    decrypted_text = reverse_binary("secret_message_file.txt")

    with open("secret_message_file.txt", "r") as f:
        secret_message = f.read().strip()

    print(f"your secret message:\n {secret_message}")

    
    print(f" Your decrypted message is: {decrypted_text}")

program()


