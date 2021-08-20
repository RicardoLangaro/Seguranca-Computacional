from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Por exemplo, é assim que você gera um novo par de chaves DSA,
# salva a chave pública em um arquivo chamado public_key.pem,
# assina uma mensagem (com Crypto.Signature.DSS) e a verifica:
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html

# As assinaturas digitais baseiam-se na criptografia de chave pública:
# quem assina a mensagem possui a chave privada e quem verifica a assinatura é a chave pública.

# *** O algoritmo só pode ser usado para autenticação (assinatura digital).
# O DSA não pode ser usado para fins de confidencialidade (criptografia).

# Criando uma chave DSA
pri_key = DSA.generate(2048)
f = open("public_key.pem", "w")
print(pri_key.export_key().decode('UTF-8'))     #converte bytes para string
print(pri_key.publickey().export_key().decode('UTF-8'))
f.write(pri_key.publickey().export_key().decode('UTF-8'))
f.close()

# Assinando a mensagem
message = b"Esta mensagem e apenas um Teste! @#$%*()(*&$#@. Mensagem Clara."
hash_obj = SHA256.new(message)
signer = DSS.new(pri_key, 'fips-186-3')     # Padrão de Assinatura Digital (DSS)
signature = signer.sign(hash_obj)
print('Assinatura digital com DSA :\nHash SHA256 \t',hash_obj.hexdigest(),'\nAssinatura \t',signature)

# Recebe (signature ,public_key)
# Carregando a chave publica. repete o processo de carregar a chave e gerar a hash como se fosse o receptor
f = open("public_key.pem", "r")
hash_obj = SHA256.new(message)
pub_key = DSA.import_key(f.read())
signer = DSS.new(pub_key, 'fips-186-3')     # Padrão de Assinatura Digital (DSS)

# Verificando sua autenticidade 1
try:
    signer.verify(hash_obj, signature)
    print ("Mensagem 1 é autentica.")
except ValueError:
    print ("Mensagem 1 não é autentica.")
finally:

    # Verificando sua autenticidade 2, sem assinar
    message = b"Mensagem nao assinada! @#$%*()(*&$#@. Mensagem Clara."
    hash_obj = SHA256.new(message)

    try:
        signer.verify(hash_obj, signature)
        print ("Mensagem 2 é autentica.")
    except ValueError:
        print ("Mensagem 2 não é autentica.")
    finally:

        # Verificando sua autenticidade 3, assinada com outra chave
        message = b"Mensagem assinada com outra chave! @#$%*()(*&$#@. Mensagem Clara."
        pri_key = DSA.generate(2048)
        hash_obj2 = SHA256.new(message)
        signer = DSS.new(pri_key, 'fips-186-3')     # Padrão de Assinatura Digital (DSS)
        signature = signer.sign(hash_obj2)

        try:
            signer.verify(hash_obj, signature)
            print ("Mensagem 3 é autentica.")
        except ValueError:
            print ("Mensagem 3 não é autentica.")