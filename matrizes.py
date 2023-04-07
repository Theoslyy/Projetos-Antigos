matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Insira o número {i}{j}: "))
diagonal = True
for i in range(3):
    for j in range(3):
        if (i != j) and (matriz[i][j] != 0):
            diagonal = False
print(diagonal)