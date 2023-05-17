#Leia o valor de um produto e mostre o valor com 5% de desconto
produto = float(input('Valor do produto: R$'))
desconto = produto - (produto * 5/100)
print('R${:.2f} com 5% de desconto: R${:.2f}'.format(produto,desconto))