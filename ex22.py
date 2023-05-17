#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1º O nome com todas as letras maiusculas
#2º O nome com todas minusculas
#3º Quantas letras ao todo (sem considerar os espaços)
#4º Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiusculo {}'.format(nome.upper())) #1
print('Seu nome em minusculo {}'.format(nome.lower())) #2
print('Seu nome tem ao total de {} letras'.format(len(nome) - nome.count(' '))) #3
print('Seu primeiro nome tem {} letras'.format(nome.find(" "))) #4

