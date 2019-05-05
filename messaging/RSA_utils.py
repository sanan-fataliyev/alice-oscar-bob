import base64
from Crypto.PublicKey import RSA

# This module contains handy functions to work with RSA
# Native RSA operations requires byte array (because they are more computation friendly)
# We defined wrapper functions (encrypt_text, decrypt_text) to work only with strings
# They use base64 encoding for string/byte


def generate_RSA_key_pairs():
    """
    Generates RSA public/private key pair and returns them as tuple
    """
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    return private_key, public_key


def encrypt_text(plain_text, public_key):
    """
    Encrypts given plain text and returns in base64 encoded
    """
    # get bytes from original text
    original_bytes = plain_text.encode()

    # encrypt bytes with given RSA public key
    encrypted_bytes = public_key.encrypt(original_bytes, 0)[0]

    # result is also bytes, but we encode it with base64
    # because strings is more print friendly than bytes
    base64text = base64.b64encode(encrypted_bytes).decode()
    return base64text


def decrypt_text(encrypted_text, private_key):
    """
    Decrypts given RSA-encrypted+base64-encoded text and returns plain text
    """
    # revert from base64 to bytes
    encrypted_bytes = base64.b64decode(encrypted_text)

    # decrypt bytes with given RSA private key
    original_bytes = private_key.decrypt(encrypted_bytes)

    # decode original text from bytes
    plain_text = original_bytes.decode()
    return plain_text
