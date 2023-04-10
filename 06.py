alunos = {}
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota
media = sum(alunos.values()) / len(alunos)
print("A média das notas é:", media)