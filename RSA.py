from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool

texto = "TeXtO dE eXeMpLo pArA eNcRiPtAr!"
pool = RandomPool(384)
pool.stir()

# randfunc deve retornar uma string de dados aleatórios de comprimento n
randfunc = pool.get_bytes

# Tamanho da chave, em bits
N = 1024
K = ""

print('Texto limpo:\t\t', texto, '\n')
# Geramos a chave (contendo a chave pública e privada):
key = RSA.generate(N, randfunc)

# Criptografando com a chave privada:
enc = key.encrypt(texto.encode(), K)
print('Encriptando com Chave Privada\t\t', enc, '\n')
# Decriptografando com a chave privada:
dec = key.decrypt(enc)
print('Decriptando com Chave Privada\t\t', dec.decode(), '\n')

# Separando apenas a chave pública:
pub_key = key.publickey()

# Criptografando com a chave pública:
enc = pub_key.encrypt(texto.encode(), K)
print('Encriptando com Chave Publica\t\t', enc, '\n')
# Decriptografando com a chave privada:
dec = key.decrypt(enc)
print('Decriptando com Chave Publica\t\t', dec.decode(), '\n')

# Recriando a chave pública com informações da chave privada:
n, e = key.n, key.e
pub_key = RSA.construct((n, e))
print('private_key\t', key, '\npub_key\t\t', pub_key)
