## Peça um número e calcule seu fatorial. O fatorial de 5 é 5 × 4 × 3 × 2 × 1 = 120.

num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é: {fatorial}")
