x = str(input("Qual o binário?"))
tamanho = len(x)
expoente = tamanho
binario = list(x)
variavel1 = 0
decimal = 0
i = 1
a = 0
for i in range(1,tamanho,1):
    if '1' in binario[a]:
        decimal = 2**(expoente-i) + variavel1
        variavel1 = decimal
    a += 1
if binario[len(x)-1] == '1':
    decimal = decimal + 1
print(decimal)