contagem = 0
pares = 0
impar = 0

while contagem < 10:
    if contagem % 2 == 0:
        pares += 1
    else:
        impar += 1
    contagem += 1
print(f"Pares: {pares}")
print(f"Impares: {impar}")