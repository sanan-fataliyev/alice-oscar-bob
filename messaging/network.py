from messaging import RSA_utils
from messaging.cryp import AESCipher
from messaging.other import introduce


class PublicNetwork:
    """
    Very insecure network. Even worse than Internet
    Everyone in this network will be get new messages/keys regardless of the target
    Can we communicate securely over this network with the help of Cryptography? Of course we can!
    """

    def __init__(self, name):
        self.name = name
        self.people = []

    @introduce
    def join(self, person):
        print(f'{person.name} joined')
        self.people.append(person)

    @introduce
    def send_message(self, message):
        print('- Sending message...')
        print(message)

        # send to all people (except to sender itself)
        for person in self.people:
            if person is not message.sender:
                person.accept_message(message)

    @introduce
    def send_symmetric_key(self, message):
        print('- Sending symmetric key...')
        print(message)

        # send to all people (except to sender itself)
        for person in self.people:
            if person is not message.sender:
                person.accept_symmetric_key(message)

    def __str__(self):
        return self.name


class Person:
    def __init__(self, name, is_bad_man=False):
        self.name = name

        # if a person is a "bad man", he/she will TRY to violate others' privacy, read their messages
        self.is_bad_man = is_bad_man

        # these RSA keys will be used for secure key delivery operation
        self.__private_key, self.public_key = RSA_utils.generate_RSA_key_pairs()

        # This dict will keep symmetric keys for each partner that we shared via RSA encryption
        # Before sending a message, we will check if there's already a shared symmetric key exchanged for that person
        # if we have, we will encrypt message before sending (see send_message method)
        # Also, when we receive an encrypted message, we will look for key in this dict to decrypt it.
        self.secure_partners = {}

    @introduce
    def exchange_key_with(self, other_person, sym_key, network):
        print(f'- I\'m trying to share my symmetric key "{sym_key}" with {other_person.name}')
        print('- After we share this key, we\'ll able to communicate securely even over insecure network')
        print(f'- But this key must be send in secure way that nobody can get it except {other_person.name}!')
        print(f"- To achieve this, I'll encrypt it with {other_person.name}\'s RSA public key before sending")

        encrypted_key = RSA_utils.encrypt_text(sym_key, other_person.public_key)
        msg = Message(encrypted_key, self, other_person, is_encrypted=True)
        network.send_symmetric_key(msg)
        self.secure_partners[other_person.name] = AESCipher(sym_key)

    @introduce
    def accept_symmetric_key(self, message):

        if message.to_person != self:
            print("- I cannot decrypt this RSA encrypted key since I don't own the private key")
        else:
            sender_name = message.sender.name
            print(f'- Okay, it seems {sender_name} wants to chat with me in more secure way.')
            key = RSA_utils.decrypt_text(message.data, self.__private_key)
            self.secure_partners[sender_name] = AESCipher(key)
            print(f'- From now, i will use the "{key}" to encrypt/decrypt my further messages with {sender_name}')

    @introduce
    def accept_message(self, message):

        if message.to_person == self:
            print(f'- I got new message from {message.sender.name}!')
        else:
            print('- This message is not for me.')

            if not self.is_bad_man:
                print("- So, I'm ignoring")
                return
            else:
                print('- But I will try to intercept it, cuz i\'m a bad man!')

        if message.is_encrypted:
            print(f'- The message is encrypted: {message.data}')
            cipher = self.secure_partners.get(message.sender.name)
            if cipher is None:
                print("- But I don't have a key to decrypt it -_-")
            else:
                print("- And I have a key to decrypt it")
                decrypted_text = cipher.decrypt(message.data)
                print(f'- Decrypted! Text is: "{decrypted_text}"')
        else:
            print('- The message is not encrypted')
            print(f'- Text is: "{message.data}"')

    @introduce
    def send_message(self, to_person, plain_text, network):
        print(f'- Sending a message to {to_person.name} over {network}')
        data, is_encrypted = plain_text, False

        cipher = self.secure_partners.get(to_person.name)

        if cipher is not None:
            data = cipher.encrypt(plain_text)
            is_encrypted = True

        msg = Message(data, self, to_person, is_encrypted=is_encrypted)
        network.send_message(msg)

    def __str__(self):
        return self.name


class Message:
    def __init__(self, data, sender, to_person, is_encrypted=False):
        self.sender = sender
        self.to_person = to_person
        self.data = data
        self.is_encrypted = is_encrypted

    def __str__(self):
        return '\n'.join([f'- {k} = {v}'for k, v in self.__dict__.items()])