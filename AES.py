
        # Segurança Computacional 2021
        # Aluno : Ricardo Langaro
        # Criptografia Simétrica AES - Algoritmo de Rijndael

        # Chaves de 128, 160, 192, 224 e 256 bits são suportadas pelo algoritmo Rijndael,
        # mas apenas as chaves de 128, 192 e 256 bits são padrão NIST.

import copy
mensagemclara = "00112233445566778899aabbccddeeff"        # exemplo http://lpb.canb.auug.org.au/adfa/src/AEScalc/index.html
chave = "000102030405060708090a0b0c0d0e0f"
# mensagemcifrada = "69c4e0d86a7b0430d8cdb78070b4c55a"

# mensagemclara = "50414c4553545241204e4f204c4e4343"      # exemplo O algoritmo AES: Apresentacao e Descricao da Estrutura.
# chave = "424f4c534953544120444f20434e5071"              # Raquel de A. de S., Fabio Borges de O., Gerson N. da C. https://bityli.com/9mlAG
# mensagemcifrada = "e6234e3a1695fb78847d99d13bcb5d94"

print("\tCriptografia Simétrica AES - Algoritmo de Rijndael")
nbits = 128;    print("Tamanho da chave: 128")
modo = input("Modo de cifragem ECB ou CBC: ")
mensagemclara = input("Mensagem clara (0-9a-f), qualquer tamanho: ")
chave = input("Chave de %d bites (0-9a-f): " % nbits)
Nr =10

def preenche_matriz_por_coluna(n_linhas, n_colunas, valor):
    matriz = []
    x = 0
    for i in range(0, n_linhas):
        l = []
        for j in range(0, n_colunas):
            l.append(valor[x:x + 2])
            x = x + 2
        matriz.append(l)
    return matriz

def AES(mensagemclara, chave, modo, nbits, Nr):

    matriz_mensagemclara = preenche_matriz_por_coluna(4, 4, mensagemclara)
    matriz_chave = preenche_matriz_por_coluna(4, 4, chave)
    print('\nMensagem clara\t', matriz_mensagemclara, '\nChave\t\t', matriz_chave, '\nNº bits\t\t', nbits,
          '\nNº rodadas\t', Nr, '\n')

    def SubBytes(A):  # substituicao de bits pela S-box

        #         Tabela 1. S-box usada no AES | 0 1 2 3 4 5 6 7 8 9 a b c d e f
        Sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],  # 0
                ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],  # 1
                ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],  # 2
                ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],  # 3
                ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],  # 4
                ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],  # 5
                ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],  # 6
                ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],  # 7
                ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],  # 8
                ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],  # 9
                ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],  # a
                ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],  # b
                ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],  # c
                ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],  # d
                ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],  # e
                ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]  # f

        saida = Sbox[int(A[0], 16)][int(A[1], 16)]
        return saida

    def RotWordTop(Vetor): #sobe linhas de um vetor de baixo para cima
        aux = Vetor[0]
        for i in range(0,len(Vetor)-1):
            Vetor[i] = Vetor[i+1]
        Vetor[len(Vetor)-1] = aux
        return Vetor

    def ShiftRows(Matriz): # da direita para esquerda
        aux = 0
        for i in range(0,4):           # coluna
            for num in range(0,i):      # numero de avanços á esquerda da linha
                aux = Matriz[0][i]
                for j in range(0,4-1): # linha
                   Matriz[j][i] = Matriz[j+1][i]
                Matriz[4-1][i] = aux
        return Matriz

    def MixColumns(Matriz):

        R = copy.deepcopy(matriz_mensagemclara)  # copia elemento a elemento, segura para matrizes e vetores
        MatrixMixColumns = [[2, 1, 1, 3], [3, 2, 1, 1], [1, 3, 2, 1], [1, 1, 3, 2]]
        # 3 = (x+1) *(Matriz)   # multiplicacao polinomial por Corpo de Galois
        # 2 =     x *(Matriz)
        # 1 =     1 *(Matriz)
        for i in range(0, 4):  # linha
            k = 0
            for k in range(0, 4):  # repete multiplicação para cada coluna
                result = 0          # resultado decimal l*c
                for j in range(0, 4):      # coluna

                    if MatrixMixColumns[j][i] == 3:
                        temp1 = (int(Matriz[k][j], 16) << 1) ^ int(Matriz[k][j], 16)  # SHIFTLEFT(num,1) XOR num
                    else:
                        temp1 = MatrixMixColumns[j][i] * int(Matriz[k][j], 16)
                    if temp1 >= 256:
                        temp1 = (temp1 % 256) ^ 283  # () XOR 1 0001 1011
                    result = result ^ temp1
                    # print('\n', MatrixMixColumns[j][i], Matriz[k][j], temp1, '= ', result, '| ')
                result = result % 256
                R[k][i] = format(hex(result)[2:], '0>2')
                # print('==',result,'| ',format(hex(result)[2:], '0>2'))
        return R

    def AddRoundKey(Matriz, Key):

        R = copy.deepcopy(matriz_mensagemclara)  # copia elemento a elemento, segura para matrizes e vetores
        for i in range(0, 4):
            for j in range(0, 4):
                R[i][j] = format(hex(int(Matriz[i][j], 16) ^ int(Key[i][j], 16))[2:], '0>2') # XOR
        return R

    def KeyExpansion(Key, NumeroRodada):

        RC = ['01', '01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']  # compõem a Rcon[0][0]=RC[Nr] da rodada Nr

        W = copy.deepcopy(Key)       # copia elemento a elemento, segura para matrizes e vetores
        for i in range(4-1,-1,-1):  # decrescente
            RotWordTop(W[i])

        # print(W,'\nSubBytes')
        for i in range(0, 4):
            for j in range(0, 4):
                # print('ij ',i,j,'valor ',W[i][j][0], W[i][j][1],a,b)
                W[i][j] = SubBytes(W[i][j])
        # print(W, '\nRcon ultima coluna')

        for i in range(0, 4):  # ultima coluna
            if i == 0:
                W[0][i] = format(hex(int(W[len(W) - 1][i], 16) ^ int(Key[0][i], 16) ^ int(RC[NumeroRodada], 16))[2:], '0>2')
            else:
                W[0][i] = format(hex(int(W[len(W) - 1][i], 16) ^ int(Key[0][i], 16) ^ 0)[2:], '0>2')
                # print(W[len(W)-1][i], Key[0][i] )

        for i in range(1, 4):  # 1:fim
            for j in range(0, 4):
                W[i][j] = format(hex(int(W[i - 1][j], 16) ^ int(Key[i][j], 16))[2:], '0>2')

        print('Key %2d ' % NumeroRodada, W)
        return W

    # A cada rodada do algoritmo de cifragem, realizamos 4 etapas:
    # AddRoundKey, SubBytes, ShiftRows e MixColumns. A primeira rodada 0, começa com uma AddRoundKey somente.
    # Na ultima rodada, a operacao MixColumns é suprimida.

    A = copy.deepcopy(matriz_mensagemclara)       # copia elemento a elemento, segura para matrizes e vetores
    # Rodada 0 : etapa AddRoundKey
    key = matriz_chave
    print('Key  0 ', key)

    A = AddRoundKey(A, matriz_chave)
    print('AddRoundKey\t', A,'\n')

    for k in range(1, Nr + 1):

        # Geração de Sub-Chaves
        key = KeyExpansion(key, k)

        # cifragem : etapa SubBytes
        for i in range(0, 4):
            for j in range(0, 4):
                A[i][j] = SubBytes(A[i][j])
        print('SubBytes\t', A)

        # cifragem : etapa ShiftRows
        A = ShiftRows(A)
        print('ShiftRows\t', A)

        # cifragem : etapa MixColumns
        if k != Nr:
            A = MixColumns(A)
            print('MixColumns\t', A)

        # cifragem : etapa AddRoundKey
        A = AddRoundKey(A, key)
        print('AddRoundKey\t', A, '\n')

    mensagemcifrada = A
    print('Mensagem Cifrada\t', A)
    return A


# MAIN
while len(mensagemclara) % (nbits//4) != 0:     # preenche bloco de 32 bits com '0'
    mensagemclara += '0'

if modo == 'ECB':
    for i in range(round(len(mensagemclara) / (nbits//4))):
        AES(mensagemclara[i * (nbits//4):(i + 1) * (nbits//4)], chave, modo, nbits, Nr)
        print('--------------------------------------------------------------')

elif modo == 'CBC':

    ciphertext = preenche_matriz_por_coluna(4, 4, "065a119ff3010c0377993e01213c0908")

    for i in range(round(len(mensagemclara) / (nbits//4))):
        msg = ""
        matrizmensagemclara = preenche_matriz_por_coluna(4, 4, mensagemclara[i * (nbits//4):(i + 1) * (nbits//4)])
        for i in range(0, 4):
            for j in range(0, 4):
                msg += format(hex(int(matrizmensagemclara[i][j], 16) ^ int(ciphertext[i][j], 16))[2:],
                              '0>2')  # XOR
        ciphertext = AES(msg, chave, modo, nbits, Nr)
        print('--------------------------------------------------------------')
else:
    print('Modo de cifragem incorreto!');    exit()
