#Leia temperatura em Celsiu e converta em Fahrenheit
celsiu = float(input('Digite a temperatura em Celsiu: '))
fah = 9* celsiu / 5 + 32
print ('A conversão de Celsius:{:.2f} em Fahrenheit é: {:.2f}'.format(celsiu,fah))