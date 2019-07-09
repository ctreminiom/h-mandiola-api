from config import configuration as conf
import base64


def encrypt(data):

    if not data:
        return data

    cypher = base64.b64encode(data.encode('utf-8'))

    return conf.first_key + cypher.decode("utf-8") + conf.last_key



def decrypt(data):

    if not data:
        return data

    #remove the keys
    cypher_with_out_key = data.replace(conf.first_key, "")
    cypher_with_out_last_key = cypher_with_out_key.replace(conf.last_key, "")

    data_decrypted = base64.b64decode(cypher_with_out_last_key).decode('utf-8')

    return data_decrypted
