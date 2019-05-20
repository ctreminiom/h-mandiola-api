#!/usr/bin/env python
# -*- coding: utf-8 -*-


from simplecrypt import encrypt, decrypt
from config import config
from base64 import b64encode, b64decode


def encode(data):
    cipher = encrypt(config.encypt_key, data)

    cipher_as_base64 = b64encode(cipher)
    cipher_as_string = cipher_as_base64.decode("utf-8") 

    return cipher_as_string


def decode(data):
    cipher = b64decode(data)

    plaintext = decrypt(config.encypt_key, cipher)

    return plaintext.decode("utf-8")






    