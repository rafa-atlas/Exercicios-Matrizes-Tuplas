
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
print("Programa para verificar se uma matriz é identidade.")
print("")

# Entrada de dados
QTDE_LINHAS = 3
QTDE_COLUNAS = 3

m = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)

for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        m[i][j] = int(input(f"Informe o valor da linha {i + 1} e coluna {j + 1}: "))

# Processamento
identidade = True

for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        if i == j and m[i][j] != 1:
            identidade = False
        elif i != j and m[i][j] != 0:
            identidade = False

# Saída de dados
print("")
print("Matriz informada:")
exibe_matriz(m)

if identidade:
    print("A matriz é identidade.")
else:
    print("A matriz não é identidade.")
