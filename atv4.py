n = int(input("Digite a quantidade de participantes:"))
somaIdade = 0
mediaIdades = 1

for i in range(n):
    idade = int(input(f"Digite a idade do participante {i+1}:"))

    somaIdade += idade

mediaIdades = somaIdade / n

print(f"A média  das idades é {mediaIdades}")

if mediaIdades <= 25:
    print("turma jovem")
elif  mediaIdades  >= 26 and mediaIdades <= 60:
    print("turma adulta")
else:
    print("turma idosa")
