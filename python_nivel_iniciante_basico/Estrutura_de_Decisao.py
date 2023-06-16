aluno=str(input("Digite o nome do aluno: "))
nota1=float(input("Digite a primeira nota obtida: "))
nota2=float(input("Digite a segunda nota obtida: "))
media=(nota1+nota2)/2
print("A nota média do", aluno, "é: ",media)
if media>=7:
    print("O ",aluno," está aprovado!")
else:
    print("O ",aluno, "está reprovado!")