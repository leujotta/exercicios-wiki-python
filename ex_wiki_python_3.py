# -*- coding: utf-8 -*-
"""ex wiki python 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W9POrnJY6_kZTFGIQGN879mtfY43K0e-

1 Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

while True:
  numero =float(input('digite um numero:'))
  if numero <= 10:
    print('valido')
    break
  else: 
    print('invalido')

"""2 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""

while True:
   user = str(input('usuario: '))
   senha = str(input('senha: '))
   if user != senha:
    print('senha aceita')
    break
   else:
     print('senha invalida')

"""3 Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;

Idade: entre 0 e 150;

Salário: maior que zero;

Sexo: 'f' ou 'm';

Estado Civil: 's', 'c', 'v', 'd';

"""

while True:
  nome = str(input('digite um nome:'))
  if len(nome) >= 3:
    print(nome)
    break
  else:
    print('invalido')

while True:
  idade = int(input('digite uma idade:'))
  if idade >= 0 and idade <= 150:
    print(idade)
  break
else:
     print('invalido')

while True:
  salario = float(input('digite o salario:'))
  if salario > 0:
    print(salario)
    break
  else:
    print('invalido')

while True:
  sexo = str(input('digite o sexo:'))
  if sexo == 'f' or sexo == 'm':
    print(sexo)
    break
  else:
   print('invalido')

while True:
  estado_c = str(input('digite o estado civil:'))
  if estado_c == 's' or estado_c == 'c' or estado_c == 'v' or estado_c == 'd':
    print(estado_c)
    break
  else:
    print('invalido')

""" 4 Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

paisA = 80000
paisB = 200000
anos = 0
crescimentoA  = 1.03
crescimentoB =  1.015

while paisA < paisB:
 paisA *= crescimentoA 
 paisB *= crescimentoB
 anos += 1
print('precisou de' , anos , 'anos pra ultrapassar')

"""5 Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

paisA =int(input('qual a população do pais A?'))
paisB = int(input('qual a população do pais B?'))
anos = 0
crescimentoA  = float(input('qual a taxa de crescimento do pais A?'))
crescimentoB =  float(input('qual a taxa de crescimento do pais B?'))

while paisA < paisB:
 paisA *= crescimentoA 
 paisB *= crescimentoB
 anos += 1
print('precisou de' , anos , 'anos pra ultrapassar')

"""6 Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro."""

numeros = []
num = 0

while num < 20:
  num += 1
  print(num)
  numeros.append(num)
print(numeros)

""" 7 Faça um programa que leia 5 números e informe o maior número."""

lista = []

while len(lista) < 5:
  lista.append(int(input('insira um número:')))
max(lista)

""" 8 Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista = []

while len(lista) < 5:
  lista.append(int(input('insira um número:')))

media = 0
for num in lista:
   media += num
print('a soma é:' , media)
print('a media é:' , media / len(lista))

"""9 Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""

numeros = []
num = 0

while num < 50:
  num += 1
  if num % 2:
   numeros.append(num)
print(numeros)

"""10 Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""

numeros = []
numero = int(input('coloque o numero inicial:'))
numero2 = int(input('coloque o numero final:'))

while numero < numero2 - 1:
  numero += 1
  numeros.append(numero)
print(numeros)

"""11 Altere o programa anterior para mostrar no final a soma dos números."""

numeros = []
numero = int(input('coloque o numero inicial:'))
numero2 = int(input('coloque o numero final:'))

while numero < numero2 - 1:
  numero += 1
  numeros.append(numero)
print(numeros)

soma = 0
for num in numeros:
 soma += num
print('soma:' , soma)

"""12 Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:"""

tabuada = int(input('digite um numero de 1 a 10 para gerar a tabuada:'))
num = 0
print('tabuada do' , tabuada)

while num < 10:
  num += 1
  print(tabuada , 'x' , num ,  '=' , tabuada * num)

"""13 Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem."""

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1

for i in range(expoente):
    resultado *= base

print(base, "elevado a", expoente, "é igual a", resultado)

"""14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade e números pares e a quantidade de números impares."""

numeros_impar = []
numeros_par = []
numero = int(input('digite um numero'))
num = 0

while num < numero:
  num += 1
  if num % 2:
   numeros_impar.append(num)
  else:
    numeros_par.append(num)

print('existem' , len(numeros_par) , 'numeros pares e eles sao:' , numeros_par)
print('existem' , len(numeros_impar) , 'numeros impares e eles sao:' , numeros_impar)

"""15 A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo."""

lista_fib = []
termo = int(input('digite o termo requerido para a sequencia de fibonacci:'))
a = 1
fibo = (a - 1) + (a - 2)

while termo > 0:
  termo -= 1
  a += 1
  lista_fib.append(a)
print(lista_fib)