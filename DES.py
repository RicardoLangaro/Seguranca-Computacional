# Materia : SEGURANÇA COMPUTACIONAL 2021
# Aluno: RICARDO LANGARO
# Criptografia DES - Data Encryption Standard
# referencia : http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm

# Input 0123456789ABCDEF    Key   133457799BBCDFF1    Out   0x85e813540f0ab405
# Input 675A69675E5A6B5A    Key   5B5A57676A56676E    Out   0x974AFFBF86022D1F

# Function to find the  XOR of the two Binary Strings
def xor(a, b, n):
    ans = ""
    for i in range(n):
        # If the Character matches
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

print('------------------------------------Criptografia DES--------------------------------')
# DES é uma cifra de bloco - o que significa que opera em blocos de texto simples de
# um determinado tamanho (64 bits) e retorna blocos de texto cifrado do mesmo tamanho.
# deve ser blocos de 64bits/4bits = 16bits hexadecimal
entradahex = '0123456789ABCDEF'
entradabin = ''
K = '133457799BBCDFF1'      # chave 16bytes
Kbin = ''
C0 = 0
D0 = 0

# matriz de transformacao PC-1
PC1 = [57, 49, 41, 33, 25, 17, 9, 1,
       58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 27, 19, 11, 3,
       60, 52, 44, 36, 63, 55, 47, 39,
       31, 23, 15, 7, 62, 54, 46, 38,
       30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 28, 20, 12, 4]

for i in range(0,len(entradahex)):
    entradabin += format(int(entradahex[i], 16), '0>4b')
    Kbin += format(int(K[i], 16), '0>4b')

print('\nM de entrada bin: ', entradabin,'\nM de entrada Hex: ',entradahex)
Km = ''
for i in PC1:           # permutação de 56 bits
    Km += Kbin[i-1]
print('K\t',Kbin,'\nKm\t',Km)

C0 = Km[:28]    # meia chave de 28 bits
D0 = Km[28:]
print('C0\t', C0, ' ', '\nD0 ', D0,'\n')

# formar 16 chaves atraves do deslocamento da primeira
# Número da Iteração / Número de deslocamentos à esquerda
#       1 1
#       2 1
#       3 2
#       4 2
#       5 2
#       6 2
#       7 2
#       8 2
#       9 1
#      10 2
#      11 2
#      12 2
#      13 2
#      14 2
#      15 2
#      16 1
C1 = C0[1:] + C0[0]
D1 = D0[1:] + D0[0]
C2 = C1[1:] + C1[0]
D2 = D1[1:] + D1[0]
C3 = C2[2:] + C2[:2]
D3 = D2[2:] + D2[:2]        # [:x] na0 pega a ultima posicao
C4 = C3[2:] + C3[:2]
D4 = D3[2:] + D3[:2]
C5 = C4[2:] + C4[:2]
D5 = D4[2:] + D4[:2]
C6 = C5[2:] + C5[:2]
D6 = D5[2:] + D5[:2]
C7 = C6[2:] + C6[:2]
D7 = D6[2:] + D6[:2]
C8 = C7[2:] + C7[:2]
D8 = D7[2:] + D7[:2]
C9 = C8[1:] + C8[0]
D9 = D8[1:] + D8[0]
C10 = C9[2:] + C9[:2]
D10 = D9[2:] + D9[:2]
C11 = C10[2:] + C10[:2]
D11 = D10[2:] + D10[:2]
C12 = C11[2:] + C11[:2]
D12 = D11[2:] + D11[:2]
C13 = C12[2:] + C12[:2]
D13 = D12[2:] + D12[:2]
C14 = C13[2:] + C13[:2]
D14 = D13[2:] + D13[:2]
C15 = C14[2:] + C14[:2]
D15 = D14[2:] + D14[:2]
C16 = C15[1:] + C15[0]
D16 = D15[1:] + D15[0]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

K1='';K2='';K3='';K4='';K5='';K6='';K7='';K8='';K9='';K10='';K11='';K12='';K13='';K14='';K15='';K16='';
# Cada par tem 56bits, mas o PC-2 usa apenas 48 deles
# faz a permutacao das 17 chaves com a vetor PC2

for i in range(1, 17):
    for j in PC2:       # permutação de 56 bits
        if i == 1:
            temp = C1 + D1
            K1 += temp[j - 1]
        elif i == 2:
            temp = C2 + D2
            K2 += temp[j - 1]
        elif i == 3:
            temp = C3 + D3
            K3 += temp[j - 1]
        elif i == 4:
            temp = C4 + D4
            K4 += temp[j - 1]
        elif i == 5:
            temp = C5 + D5
            K5 += temp[j - 1]
        elif i == 6:
            temp = C6 + D6
            K6 += temp[j - 1]
        elif i == 7:
            temp = C7 + D7
            K7 += temp[j - 1]
        elif i == 8:
            temp = C8 + D8
            K8 += temp[j - 1]
        elif i == 9:
            temp = C9 + D9
            K9 += temp[j - 1]
        elif i == 10:
            temp = C10 + D10
            K10 += temp[j - 1]
        elif i == 11:
            temp = C11 + D11
            K11 += temp[j - 1]
        elif i == 12:
            temp = C12 + D12
            K12 += temp[j - 1]
        elif i == 13:
            temp = C13 + D13
            K13 += temp[j - 1]
        elif i == 14:
            temp = C14 + D14
            K14 += temp[j - 1]
        elif i == 15:
            temp = C15 + D15
            K15 += temp[j - 1]
        elif i == 16:
            temp = C16 + D16
            K16 += temp[j - 1]

print('K1\t', K1)
print('K2\t', K2)
print('K3\t', K3)
print('K4\t', K4)
print('K5\t', K5)
print('K6\t', K6)
print('K7\t', K7)
print('K8\t', K8)
print('K9\t', K9)
print('K10\t', K10)
print('K11\t', K11)
print('K12\t', K12)
print('K13\t', K13)
print('K14\t', K14)
print('K15\t', K15)
print('K16\t', K16)

# permutação da mensagem inicial M pelo vetor IP
IP = [  58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

Ip = ''
for i in IP:           # permutação de 56 bits
    Ip += entradabin[i-1]

L0 = Ip[:32]  # esquerdo
R0 = Ip[32:]  # direito
print('\nentrada\t', entradabin, '\n', '\rIp\t\t', Ip)
print('L0\t', L0, '\nR0\t', R0)

# Para os 32 bits direitos na etapa atual, XOR com os 32 bits esquerdos da etapa anterior e cálculo f
E = [32, 1, 2, 3, 4, 5,  # matriz permutação - expansão
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16,  7, 20, 21,
	 29, 12, 28, 17,
	  1, 15, 23, 26,
	  5, 18, 31, 10,
	  2,  8, 24, 14,
	 32, 27,  3, 9 ,
	 19, 13, 30, 6 ,
	 22, 11,  4, 25]
# Caixas S
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6,  1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7,  0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
# Cada grupo de seis bits nos dará um endereço em uma caixa S diferente .
# Localizado nesse endereço, haverá um número de 4 bits. Este número de
# 4 bits substituirá os 6 bits originais. O resultado líquido é que os
# oito grupos de 6 bits são transformados em oito grupos de 4 bits
# para uma saida de 32 bits.

def S(Rout):
    B1 = Rout[0:6]
    B2 = Rout[6:12]
    B3 = Rout[12:18]
    B4 = Rout[18:24]
    B5 = Rout[24:30]
    B6 = Rout[30:36]
    B7 = Rout[36:42]
    B8 = Rout[42:48]
    return(format(S1[int(B1[0] + B1[5], 2)][int(B1[1:5], 2)], '0>4b') +     # conversão base 2 para base 10
           format(S2[int(B2[0] + B2[5], 2)][int(B2[1:5], 2)], '0>4b') +
           format(S3[int(B3[0] + B3[5], 2)][int(B3[1:5], 2)], '0>4b') +
           format(S4[int(B4[0] + B4[5], 2)][int(B4[1:5], 2)], '0>4b') +
           format(S5[int(B5[0] + B5[5], 2)][int(B5[1:5], 2)], '0>4b') +
           format(S6[int(B6[0] + B6[5], 2)][int(B6[1:5], 2)], '0>4b') +
           format(S7[int(B7[0] + B7[5], 2)][int(B7[1:5], 2)], '0>4b') +
           format(S8[int(B8[0] + B8[5], 2)][int(B8[1:5], 2)], '0>4b'))

def f(R, K, c):  # expande 32 bits para 48 bits
    Rout = ''; Pout = ''
    cont = 0
    for i in E:     # permutacao E
        Rout += str(int(K[cont]) ^ int(R[i - 1]))  # XOR bit a bit
        cont += 1
    s = S(Rout)
    for i in P:  # permutação P em cima de S(R,K)
        Pout += s[i - 1]
    print('\nR', c, '\t\t', R, '\nf', c, '\t', Rout, '\nSout', c, '\t', s, '\nPout', c, '\t', Pout)

    return Pout  # 48 bits

# rodadas caixas S
L1 = R0
R1 = xor(L0, f(R0, K1, 1), 32)
L2 = R1
R2 = xor(L1, f(R1, K2, 2), 32)
L3 = R2
R3 = xor(L2, f(R2, K3, 3), 32)
L4 = R3
R4 = xor(L3, f(R3, K4, 4), 32)
L5 = R4
R5 = xor(L4, f(R4, K5, 5), 32)
L6 = R5
R6 = xor(L5, f(R5, K6, 6), 32)
L7 = R6
R7 = xor(L6, f(R6, K7, 7), 32)
L8 = R7
R8 = xor(L7, f(R7, K8, 8), 32)
L9 = R8
R9 = xor(L8, f(R8, K9, 9), 32)
L10 = R9
R10 = xor(L9, f(R9, K10, 10), 32)
L11 = R10
R11 = xor(L10, f(R10, K11, 11), 32)
L12 = R11
R12 = xor(L11, f(R11, K12, 12), 32)
L13 = R12
R13 = xor(L12, f(R12, K13, 13), 32)
L14 = R13
R14 = xor(L13, f(R13, K14, 14), 32)
L15 = R14
R15 = xor(L14, f(R14, K15, 15), 32)
L16 = R15
R16 = xor(L15, f(R15, K16, 16), 32)

# permutação final IP -1
IP1 = [40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57, 25]

cifrada = ''
for i in IP1:       # permutação de 64 bits
    cifrada += (R16+L16)[i-1]

print('\nM cifrada bin: \t', cifrada, '\nM cifrada Hex:', hex(int(cifrada, 2)))
