# seguranca-computacional
Algoritmo de criptografia DES (Data Encryption Standard)

Um dos algoritmos mais conhecidos da área. Conhecido como criptografia simétrica. Atua em blocos de 64 bits de entrada e devolve 64 bits de saída.

-------------
Dada Entrada:   0123456789ABCDEF    
Key:   133457799BBCDFF1    
Saída:   0x85e813540f0ab405

-----------
Dada Entrada:   675A69675E5A6B5A    
Key:   5B5A57676A56676E    
Saída:   0x974AFFBF86022D1F

Mais informações podem serem encontradas em http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm

-------------
Algoritmo de criptografia AES (Advanced Encryption Standard)

Criptografia simétrica, sucessor do antigo DES com estrutura mais complexa e capacidade de chave expandida. Padronizada pelo NIST, a criptografia AES suporta de 128, 192 e 256 bits como chave oficialmente. Suporta encriptação no modo ECB (cifra de blocos de dados independentementes) e CBC (cifra de blocos de dados encadeados). Atua em blocos de 128 bits de entrada e devolve 128 bits de saída.

-------------
Dada Entrada:   00112233445566778899aabbccddeeff    
Key:   000102030405060708090a0b0c0d0e0f    
Saída:   69c4e0d86a7b0430d8cdb78070b4c55a

-----------
Dada Entrada:   50414c4553545241204e4f204c4e4343    
Key:   424f4c534953544120444f20434e5071    
Saída:   e6234e3a1695fb78847d99d13bcb5d94

-------------
Algoritmo de criptografia RSA (Rivest Shamir Adleman)

Exemplo de criptografia assimétrica de texto utilizando o conceito de par de chaves pública e privada com a biblioteca Crypto.

-------------
Algoritmo de Assinatura Digital DSA (ElGamal)

DSA é um algoritmo de assinatura de chave pública amplamente difundido. O algoritmo só pode ser usado para autenticação (assinatura digital), não pode ser usado para confidencialidade (criptografia).

Exemplo de assinatura para mensagem de texto e verificação por chave pública usando a biblioteca Crypto.
