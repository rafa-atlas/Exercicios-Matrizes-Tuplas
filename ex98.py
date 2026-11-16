
def cria_matriz(linhas, colunas):
    x = list()
    for i in range(linhas):
        x.append([0] * colunas)
    return x


def exibe_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:10.2f}", end="")
        print("")


# Apresentação
print("Programa para somar duas matrizes 4 x 3.")
print("")

# Entrada de dados
QTDE_LINHAS = 4
QTDE_COLUNAS = 3

m1 = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)
m2 = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)
soma = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)

print("Informe os valores da primeira matriz:")
for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        m1[i][j] = float(input(f"Valor da linha {i + 1}, coluna {j + 1}: "))

print("")
print("Informe os valores da segunda matriz:")
for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        m2[i][j] = float(input(f"Valor da linha {i + 1}, coluna {j + 1}: "))

# Processamento
for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        soma[i][j] = m1[i][j] + m2[i][j]

# Saída de dados
print("")
print("Resultado da soma:")
exibe_matriz(soma)
