# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = 'KLI820EBCHJWPLQ985N10C0C74LE338Q'.encode('utf8')
clearmensage = 'Mensagem a ser criptografado!'.encode('utf8')
modo = AES.MODE_EAX

# Driptografia
# uma chave unica de verificacao é gerada, não deve ser reutilizada
nonce = get_random_bytes(8)
cipher = AES.new(key, modo, nonce=nonce)
# nonce = cipher.nonce

ciphertext = cipher.encrypt(clearmensage).hex()

print( 'nonce\t', nonce, nonce.hex(), bytes.fromhex(nonce.hex()) )
print( clearmensage.decode('utf8'),'\t', key.decode('utf8') ,'\t' ,ciphertext)

# print( key.decode('utf8') ,'\t' ,bytes.fromhex(ciphertext) )
# Descriptografia
cipher = AES.new(key, modo, nonce=nonce)
plaintext = cipher.decrypt( bytes.fromhex(ciphertext))

print( ciphertext,'\t', key.decode('utf8'),'\t',  plaintext.decode('utf8') )
