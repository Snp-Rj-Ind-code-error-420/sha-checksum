''' sha 256 checksum checker '''
from cryptography.hazmat.primitives import hashes
import os
 
def has(key):
    
    digest = hashes.Hash(hashes.SHA256())
    digest.update(key)
    key=digest.finalize()
    return key
        
    

def checksum(path):
    try:
        
        with open(path,'rb') as m:
            msg=m.read()
            msg=has(msg)
        print(msg.hex())
    except Exception as e:
        print('error= ',e)

    
        
