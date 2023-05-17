#Leia um salario e de um aumento de 15%
salario = float(input('Digite o salario: R$'))
novsalario = salario + (salario * 15/100)
print('R${:.2f} com 15% de aumento: R${:.2f}'.format(salario,novsalario))