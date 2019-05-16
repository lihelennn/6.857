from virgil_crypto import VirgilCrypto
import sys

USERS = ['Alice', 'Bob', 'Eve']
keys_dict = {}
messages = {}
crypto = VirgilCrypto()
for user in USERS:
    key_pair = crypto.generate_keys()
    private_key = key_pair.private_key
    public_key = key_pair.public_key
    keys_dict[user] = (public_key, private_key)
# print(key_pair)


if __name__ == '__main__':
    args = sys.argv
    command = args[1]
    if command == "send":
        sender = args[2]
        receiver = args[3]
        message_to_encrypt = args[4]
        data_to_encrypt = message_to_encrypt.encode()

        receiver_public_key = keys_dict[receiver][0]
        reciver_list = [receiver_public_key]
        encrypted_data = crypto.encrypt(data_to_encrypt, *reciver_list)
        # print(type(str(encrypted_data)))
        if (sender, receiver) not in messages:
            messages[(sender, receiver)] = [encrypted_data]
        else:
            messages[(sender, receiver)].append(encrypted_data)
        print("message from " + str(sender) + " to " + str(receiver) + " stored: " + str(encrypted_data))
        # print(messages)
    elif command == "view":
        receiver = args[2]
        receiver_private_key = keys_dict[receiver][1]
        for user_pair in list(messages.keys()):
            if receiver == user_pair[1]:
                decrypted_data = crypto.decrypt(encrypted_data, receiver_private_key)
                decrypted_message = bytes(decrypted_data).decode()
                print(user_pair, decrypted_message)
