## Peça um número e exiba sua tabuada de 1 a 10.

num = int(input("Digite um número para ver sua tabuada: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
