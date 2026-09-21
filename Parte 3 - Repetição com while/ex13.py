## Peça uma senha ao usuário e continue pedindo até que ele digite senai123. Ao acertar, exiba "Acesso liberado".

senha_correta = "feuser2712"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso liberado.")