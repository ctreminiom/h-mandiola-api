#!/usr/bin/env python
# -*- coding: utf-8 -*-


from config import config
import base64


def encode(data):
    cipher = base64.b64encode(data.encode('utf-8'))

    return config.encypt_key_1 +  cipher.decode("utf-8") +  config.encypt_key_2





def decode(data):

    #remove the keys
    cipher_without_key_1 = data.replace(config.encypt_key_1, "")
    cipcher_without_key_2 = cipher_without_key_1.replace(config.encypt_key_2, "")

    cipher = base64.b64decode(cipcher_without_key_2).decode('utf-8')

    return cipher




'''
string = "geeks for geeks geeks geeks geeks" 
   
# Prints the string by replacing geeks by Geeks  
print(string.replace("geeks", "Geeks"))  
  
# Prints the string by replacing only 3 occurence of Geeks   
print(string.replace("geeks", "GeeksforGeeks", 3)) 
'''




    