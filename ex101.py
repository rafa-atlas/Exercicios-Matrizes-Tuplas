
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
print("Programa para calcular o determinante de uma matriz 3 x 3.")
print("")

# Entrada de dados
QTDE_LINHAS = 3
QTDE_COLUNAS = 3

m = cria_matriz(QTDE_LINHAS, QTDE_COLUNAS)

for i in range(QTDE_LINHAS):
    for j in range(QTDE_COLUNAS):
        m[i][j] = float(input(f"Informe o valor da linha {i + 1} e coluna {j + 1}: "))

# Processamento
determinante = (m[0][0] * m[1][1] * m[2][2] +
                m[0][1] * m[1][2] * m[2][0] +
                m[0][2] * m[1][0] * m[2][1] -
                m[0][2] * m[1][1] * m[2][0] -
                m[0][1] * m[1][0] * m[2][2] -
                m[0][0] * m[1][2] * m[2][1])

# Saída de dados
print("")
print("Matriz informada:")
exibe_matriz(m)

print(f"Determinante: {determinante:.2f}")
