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
print("Programa para calcular o determinante de uma matriz 2 x 2.")
print("")

# Entrada de dados
QTDE_LINHAS = 2
QTDE_COLUNAS = 2

m = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)

for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        m[i][j] = float(input(f"Informe o valor para a linha {i + 1} e coluna {j + 1}: "))

# Cálculo
determinante = m[0][0] * m[1][1] - m[0][1] * m[1][0]

# Saída
print("")
print("Matriz informada:")
exibe_matriz(m)

print(f"Determinante: {determinante:.2f}")