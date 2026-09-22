## Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.

lista = [5, 12, 8, 20, 3, 15]
count = 0
for item in lista:
    if item > 10:
        count += 1
print("Quantidade de itens maiores que 10:", count)
