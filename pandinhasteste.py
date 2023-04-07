import pandas as pd
dataset = {
    'Sobremesas': ["Bolo", "Quindão", "Bolo de sorvete"],
    'Tipo': ["Básico", "Básico", "Complexo"],
    'Temperatura': ["Quente", "Gelado", "Gelado"]
}
lista = pd.DataFrame(dataset, index = ["Norma", "Theo", "Arthur"])
print(lista)