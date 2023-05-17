#Mostre os tipos da msg
n1 = input('Digite algo: ')
print('O tipo primitivo dessa variavel é: ', type(n1))
print('É um numero? ', n1.isnumeric())
print('É maiusculo? ',n1.isupper())
print('É um numero decimal? ',n1.isdecimal())
print('É minusculo? ',n1.islower())
print('É um espaço? ',n1.isspace())

# n2 = input('Se o tipo do texto é maiusculo: ')
# print(n2.isupper())