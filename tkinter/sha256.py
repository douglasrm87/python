import hashlib
senha = hashlib.sha256(b"minhasenha").hexdigest()
print ("SHA-256: ",senha)
print (len(senha))