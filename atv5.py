N = int(input("Digite a quantidade de números:"))
somaValores = 0
conjunto=[]
for i in range(N):
    valor = float(input(f"Digite o {i+1}º valor:"))
    conjunto.append(valor)
    somaValores += valor

maior = max(conjunto)
menor = min(conjunto)

print(f"Soma: {somaValores}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

