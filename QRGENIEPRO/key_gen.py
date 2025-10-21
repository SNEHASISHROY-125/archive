from cryptography.fernet import Fernet

def gen_activation_key():
    '''
    GEN RANDOM KEY -> 

    ({\n
        KEY[:5]  :  ENCRYPTED_KEY\n
    } ,\n
    ORIGINAL_KEY,\n
    )
    '''
    key = Fernet.generate_key().decode()
    return {
        key[:5] : Fernet(key).encrypt(key.encode()).decode()
    } , key

import os , json

with open("auths.json" , "r") as auth_db : keys_master = json.load(auth_db)

keys = keys_master.get("keys")


## incert generated_activation_key
key_encrypted , original_key = gen_activation_key()
# 
keys[
    tuple(key_encrypted.keys())[0]
]         =     tuple(key_encrypted.values())[0]

keys_master["keys"] = keys

## update | commit changes to auths.json
with open("auths.json" , "w") as auth: auth.write(json.dumps(keys_master , indent=4))

print("share this key:", original_key) 