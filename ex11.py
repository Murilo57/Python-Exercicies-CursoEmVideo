#Leia a altura e a largura de uma parede em metros e exiba a area e quantidade de tinta para pinta la 
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = largura * altura
tinta = area / 2 
print('O total da area é {:.2f}, considerando que 1 litro de tinta pinta 2m² você ira precisar de {:.2f}l'.format(area,tinta))