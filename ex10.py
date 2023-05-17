#Leia quanto dinheiro tem na carteira e exiba quantos dolares consegue comprar com a quantia
real = float(input('Qual o valor que quer investir: R$'))
dolar = real / 4.91
print('Com R${:.2f} você consegue comprar: U${:.2f}'.format(real,dolar))