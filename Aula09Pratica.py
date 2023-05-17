#Pratica diante da aula 9

#Fatiando strings
frase = 'Curso em Video Python'
print(frase[3:13]) #Resultando no inicio do terceiro indice até o 12º indice, no caso 13º - 1 = 12º
#Resultado = 'so em Vide'

#print("""Microsoft Corporation é uma empresa transnacional dos Estados Unidos com sede em Redmond, Washington, que desenvolve, fabrica, licencia, apoia e vende softwares de computador, produtos eletrônicos, computadores e serviços pessoais.""") #Ira imprimir toda a frase utilizando as 3 aspas duplas no inicio e no fim ao inves de fazer print pedaço por pedaço

#No python tudo é um objeto, como exemplo consigo usar funçoes dentro de um print como:

print(frase.count('o')) #Aqui ele ira contar quantos 'o' tem dentro da minha string 

#Posso utilizar mais de uma função também como:
print(frase.upper().count('o')) # Ele ira transformar toda a frase em maiusculo e contar quantos 'o's tem dentro da frase, aqui no caso ele ira retornar 0 pq eu pedi pra ele contar os 'o's em minusculo

print(len(frase)) #Ira retornar o tamanho da string ou a quantia de caractere dentro dele(Os espaços também contam)

print(frase.replace('Python','Android')) #Ele ira trocar trocar todas as palavras 'Python' dentro da string por 'Android'

#O replace não ira mudar definitivamente a frase pois uma string é imutavel, então ele ira apenas mudar no momento em que eu pedir, dali a diante a string volta a ser o q era antes 
#Para realmente mudar uma frase com o replace eu tenho q fazer a variavel string receber o replace como:

frase = frase.replace('Python','Android') #Agora sim a partir daqui a palavra Python foi mudada definitivamente

print('Curso' in frase) #O operador "In" ira verificar se ha a palavra 'Curso' dentro dessa variavel

frase = 'Curso em Video Python'
dividido = frase.split() #O split ira dividir a frase em elementos
print(dividido[3][3]) #Aqui eu pedi para ele chamar o 3º elemento da frase que no caso é 'Video' e me mostrar também a 3º letra desse elemento que é o 'd'