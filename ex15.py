#Leia a quantidade de KM percorrido e os dias que o carro esteve alugado considerando q o dia vale R$60 e o KM R$0.15

km = int(input('Quantos km foram percorrido: '))
dia = int(input('Quantos dias ficou alugado: '))
resultadokm = km * 0.15
resultadodia = dia * 60
total = resultadokm + resultadodia
print('Considerando o Km a R$0.15 e o dia R$60 o total de {}km e {} dias da = {:.2f}'.format(km,dia,total))
