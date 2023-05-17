# Código desenvolvido durante o video
# Trabalhando com variaveis e mensagens
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma do produto é {0}, a subtração é {1}, a multiplicação {2}, a divisão {3}'.format(a,s,m,d))
print('a divisão inteira {0}, a exponenciação {1} '.format(di,e))

#Código do exercicio proposto
# Mostre o sucessor e o antecessor de um numero
n1 = int(input('Digite um numero'))
ante = n1 - 1
suce = n1 + 1
print('O antecessor de {} é {}, e sucessor é {}'.format(n1,ante,suce))