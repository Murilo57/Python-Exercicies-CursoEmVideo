#Manipulando texto   17/04/2023

#Fatiamento
frase = 'Curso em video Python'

frase[9:21:2] #Nesse fatiamento ele vai contar do nono caractere até o vigezimo, pois ele pega do ultimo indice e subtrai 1, no caso ele vai contar somente até o vigezimo caractere. O terceiro numero citado é o numero de casa que ele vai pular na contagem, no caso de 2 em 2, sempre contando o segundo

#Resultado = [V d o p t o], do nono caractere até o vigezimo pulando de 2 em 2 casa

frase[:5] #Nesse caso quando não há um valor antes dos : ele começa a contar do inicio do indice, nesse caso ele começa do 0

#Resultado = [C U R S O], do indice 0 [C] até o quarto caractere [O] pois ele pega o numero do indice chamada menos 1

frase[15:] #Nesse caso o indice sem nenhum valor dps dos : ele chama o inicio do indice no caso 15 [P] e vai até o fim da frase

frase[9::3] #Nesse caso quando o segundo indice esta vazio, ele começa do nono indice, vai até o fim pois o final não foi determinado, no caso quando for vazio ele vai até o fim, e o 3 depois dos :: significa de quantas em quantas casa vão ser pulada

#Resultado = [V E P H]

#Análise = Analisar uma string significa saber algumas informaçoes sobre ela tipo, qual o tamanho dela, com que letra ela começa, com que letra ela termina, qual a primeira palavra inteira, etc.

len(frase) #Len vem de lenght que significa comprimento, ou seja, qual o comprimento dessa frase

frase.count('o') #Outra forma de analisar string é utilizando o count, nesse caso estou pedindo para que ele conte quantas letras 'o' tem dentro da minha string, ele diferencia minuscula de maiuscula

frase.count('o',0,13) #Podendo se utilizar a contagem de caractere com fatiamento, começando do indice 0 até o indice 12, que no caso seria o 13(ultimo) menos 1

frase.find('deo') #Find significa encontrar, ele vai me dizer quantas vezes dentro dessa string ele encontrou 'deo', ele vai me dizer em que posição esses caracteres começaram, no caso o D começa na posição do indice 11

frase.find('android') #Essa função ira retornar -1, ou seja sempre que eu declarar uma string no find que não existe, ele retornara -1 ao inves de false ou null

'Curso' in frase #O operador IN ira retornar se existe ou não a string dentro da variavel citada, se houver a string ele ira retornar True, caso contrario ira retornar false

#Por via de regra uma lista de string é imutavel ou seja a gente não consegue mexer nela, porém eu consigo mudar ela atrávez de metodos 
#Transformação

frase.replace('Python','Android') #Replace significa trocar/reposicionar, nesse caso ele ira procurar por "Python" e ira substituir por "Android"

frase.upper() #Upper significa pra cima ou seja ira ficar em maiusculas, o que for maiusculo ele mantém, o que não for ele substitui por maiusculo.

frase.lower() #Lower é o contrario de Upper, ele ira manter o que esta minusculo e ira pegar as letras em maiusculos e mudar para minusculo 

frase.capitalize() #Capitalize era pegar todas as letras em maiusculos e ira trocar para minusculo deixando SOMENTE a primeira letra da frase em maiusculo 

frase.title() #Diferente do capitalize, o title ira pegar TODAS as palavras na frase e ira tornar a primeira letra em maiusculo. Ele pega sempre a referencia após o espaço, ou seja toda frase que vem depois de um espaço ira ter a primeira letra maiuscula

frase = '   Aprenda Python  ' #Dentro dessa variavel agora foi declarada propositalmente com espaços antes do inicio da frase e mais espaços após o fim dela

frase.strip() #O strip ira remover todos os espaços inuteis dentro da variavel, no caso os espaços antes da frase e após o fim dela.

frase.rstrip() #De forma similar tem o Rstrip que significa RIGHT(direita) onde ira remover os espaços inuteis a direita da frase, no caso ira remover somente os espaços após o fim da frase

frase.lstrip() #De forma contraria do Rstrip o Lstrip de LEFT(esquerda) remove os espaços inuteis a esquerda da frase, ou seja do inicio da frase

frase = 'Curso em Video Python'
#Divisão, podendo dividir strings

frase.split() #Ele ira pegar onde tem spaço dentro da string e ira dividir a cada espaço, praticamente removendo os espaços e deixando cada palavras indivuduais, cada elemento é separado pelo split

#Resultado = 'Curso' 'em' 'Video' 'Python', separando a frase em elementos individuais

#Junção, diferente da divisão eu utilizo para juntar elementos, juntar strings

'-'.join(frase) #O join serve para juntar as strings que estão separadas, nesse caso declarado no inicio um '-' ele ira pegar esse traço dentro da string e ira trocar por onde deveriam ser os espaços na frase

#Resultado = De 'Curso' 'em' 'Curso' 'Python' para: 'Curso-em-Video-Python'
