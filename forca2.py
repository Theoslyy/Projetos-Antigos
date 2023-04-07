#work in progress
import random
possibilidades = ['casa','caminho','pedra','palavra']
palavra = random.choice(possibilidades)
secreto = list(palavra)
vencedor = False
palavra_final = [" "]*len(secreto)
y = input("Qual a letra? ")
tentativa = 0
while tentativa != 5 or palavra_final != secreto:
    if y in(secreto):
        for i in range(len(secreto)):
            if y == secreto[i]:
                palavra_final[i] = y
            i += 1
        print(palavra_final)
        if palavra_final == secreto:
            tentativa = 5
            vencedor = True
        y = input("Qual a letra? ")
    if y not in(secreto):
        print("Essa palavra não existe na letra.")
        tentativa = 5
    
    
    
    
    
    
    
    
    
#   y = input("Qual a palavra? ")
#    i += 1
#if y == x:
#    vencedor = True
#    print("Você venceu.")
#if vencedor == False:
#    print("Você perdeu todas as tentativas.")