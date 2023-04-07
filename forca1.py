import random
palavras = ['casa','caminho','pedra','palavra']
x = random.choice(palavras)
vencedor = False
y = input("Qual a palavra? ")
i = 0
while y != x:
    print(f"Você tem {5 - i} tentativas.")
    y = input("Qual a palavra? ")
    i += 1
if y == x:
    vencedor = True
    print("Você venceu.")
if vencedor == False:
    print("Você perdeu todas as tentativas.")