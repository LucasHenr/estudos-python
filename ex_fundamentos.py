#Ex1
'''
print("Olá Mundo")
'''

#Ex2
'''
nome = input("Qual o seu nome?")
print("É um prazer te conhecer", nome)
'''

#Ex3
'''
num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))
soma = (num1 + num2)
print(soma)
'''

#Operadores artiméticos
'''
Ordem de procedëncia 
1 - ()
2 - **
3 - * / // %
4 - + - 
'''

#Ex5
'''
num1 = int(input("Digite um número"))
antecessor = num1 - 1
sucessor = num1 + 1
print("Seu número é {} , seu antecessor é {} e seu sucessor é {}".format(num1,antecessor,sucessor))
'''

#Ex6 
'''
num1 = int(input("Digite um número"))
dobro  = num1 * 2
triplo = num1 * 3
raiz_quadrada = num1 ** (1/2)
print("O número é {} , seu dobro é {}, seu triplo {} e sua raiz quadrada {}".format(num1,dobro,triplo,raiz_quadrada))
'''

#Ex7
'''
num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))
media = (num1 + num2) / 2
print(media)
'''

#Ex8
'''
distancia = float(input("Digite a distância em metros"))
cm = distancia * 100
mm = distancia * 1000
print("A distancia é de {} metros , em cm {} e em mm {}".format(distancia,cm,mm))
'''

#Ex9 
'''
real = float(input("Digite o valor em real"))
dolar = real / 5.02
print("O {:.2f} em real corresponde a {:.2f} dólares".format(real,dolar))
'''

#Ex10
'''
largura = float(input("Qual a largura da parede"))
altura = float(input("Qual a altura da parede"))
area = largura * altura
tinta = area / 2
print("Dimensäo da parede é de {}x{} e sua área é {}, será necessário {}l de tinta".format(largura,altura,area,tinta))
'''

#Ex11
'''
valor = int(input("Digite um valor"))
desconto = valor - (valor * 15/100)
print("O valor de compra é {}, com 15% de desconto fica no total de {}".format(valor,desconto))
'''

#Ex12
'''
valor = int(input("Digite um valor"))
aumento = valor +  (valor * 25/100)
print("O valor de compra é {}, com 25% de aumento fica no total de {}".format(valor,aumento))
'''

#Ex13
'''
temperatura = int(input("Digite o valor da temperatura em celsius: "))
farenheit = (temperatura * 9/5) + 32
print("A temperatura {} , convertida para farenheit é {}".format(temperatura,farenheit))
'''

#Ex14
'''
dias_alugados = int(input("Quantos dias o carro ficou alugado: "))
km_rodados = float(input("Quantos KM rodados: "))
valor_carro = (dias_alugados * 60) + (km_rodados * 0.15)
print("O valor total do alugel do carro foi de {}".format(valor_carro))
'''

#Ex15
'''
import math
numero = float(input("Digite um número"))
print("O número é {} e sua parte inteira é {}".format(numero, math.trunc(numero)))
'''
#Ex16
'''
import math
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)   
print("O cateto oposto é {}, o adjacente é {} e a hipotenusa é {:.2F}".format(cateto_oposto,cateto_adjacente,hipotenusa))
'''

#Ex17
'''
import math
angulo = int(input("Digite um ângulo: "))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print("O ângulo é {:.2F} , seu seno é {:.2F}, sua tangente é {:.2F} e seu cosseno {:.2F}".format(angulo, seno, tangente, cosseno))
'''

#Ex18
'''
import random
aluno1 = str(input("Digite o nome do aluno: "))
aluno2 = str(input("Digite o nome do aluno: "))
aluno3 = str(input("Digite o nome do aluno: "))
aluno4 = str(input("Digite o nome do aluno: "))
lista_alunos = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(lista_alunos)
print("O aluno sorteado foi: {}".format(sorteado))
'''

#Ex19

from random import shuffle
aluno1 = str(input("Digite o nome do aluno: "))
aluno2 = str(input("Digite o nome do aluno: "))
aluno3 = str(input("Digite o nome do aluno: "))
aluno4 = str(input("Digite o nome do aluno: "))
lista_aluno = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista_aluno)
print(f"A ordem de apresentacao é {lista_aluno}")

