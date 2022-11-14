'''
c = 1
par = impar = 0


while c != 0:
    c = int(input ("DIgite um número: "))
    if c != 0:
        if c % 2 == 0:
            par += 1
        if c % 2 == 1:
            impar += 1
    
    
print (f"Par: {par} e Impar {impar}")
'''



'''
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = input ("Informe seu sexo [M/F]: ").upper().strip()
    
    print ('Dados inválidos, digite novamente!')
    print ('')
    
if sexo == 'M' or sexo == 'F':
    print (f'Sexo cadastrado {sexo} com sucesso') 
'''


'''
from random import randint, random

print ("""Sou seu COMPUTADOR
Acabei de pensar em um número
ENTRE 0 E 10
ADIVINHE!\n""")

numero = randint(0,10)
usuario = -1

while usuario != numero:
    usuario = int(input('Digite um número: '))
    if usuario < numero:
        print ("Mais... TENTE outra vez.")
    if usuario > numero:
        print ('Menos... tente outra vez')
    print('')
    
print ('Parabéns, você acertou! ')

'''



'''
primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite o 2* valor: '))

escolha = True

while escolha != 5:
    print (""" 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA\n""")
    
    escolha = int(input('Digite a opção DESEJADA: '))
    print ("")
    
    if escolha == 1:
        soma = primeiro_valor + segundo_valor
        print (f'A soma entre os NÚMEROS: {soma}')
        print ("==========================")
    if escolha == 2:
        multiplicador = primeiro_valor * segundo_valor
        print (f"A multiplicação dos NÚMEROS é: {multiplicador}\n")
        print ("===============================")
    if escolha == 3:
        if primeiro_valor > segundo_valor:
            print (f"O primeiro valor é maior. ")
            print ("===========================")
        elif segundo_valor > primeiro_valor:
            print (f'O segundo valor é maior')
            print ("=========================")
        else:
            print ('Os valores são IGUAIS')
            print ("========================")
    if escolha == 4:
        primeiro_valor = int(input("Digite um valor: "))
        segundo_valor = int (input ('Digite o 2* valor: '))
print ("\nFIM DO PROGRAMA!\n")

'''

'''
from time import sleep

numero = int(input("Fatorial de: ") )
resultado = 1
cont = 1

while cont <= numero:
    resultado = resultado * cont
    cont = cont + 1
    
print ("CALCULANDO...")
sleep(2)
print (resultado)
'''  

'''
termo =  int(input("Digite o termo: "))    
razao = int(input("Digite a razao: "))
n_termos = int(input("Digite o número de termos: "))
decimo = termo + (10-1) * razao

cont = 1

while cont <= n_termos:
    print (f"{termo}",end=' ')
    termo += razao
    cont = cont + 1
    
print ("")
acrescimo = True

while acrescimo != 0:
    acrescimo = int(input("\nQuantos termos você quer MOSTRAR a mais: "))
    cont2 = 1
    
    while cont2 <= acrescimo:
        print (f"{termo}",end=' ')
        termo += razao
        cont2 = cont2 + 1
    print ("")
'''

'''
termos = int(input("Digite a quantidade de TERMOS: "))

anterior = 0
proximo = 1
contador = 2

print (f"{anterior}",end=' ') 

while contador <= termos:
    print (f'{proximo}',end=' ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    contador = contador + 1
print ("\n")
'''

'''
numero = 0
soma = 0

while numero != 999:
    numero = int(input('Digite 999 para PARAR: '))
    if numero != 999:
        soma+=numero
print (soma)
'''       
    
'''
numero = []
letra = 'S'
soma = 0
cont = 0

while letra == 'S':
    n = int(input("Digite um número: "))
    numero.append(n)
    soma+=n
    letra = input("Quer continuar? [S/N]: ").upper().strip()[0]
    cont += 1
if letra != 'S':
    resultado = soma / cont
    print (f'Você digitou {cont} números, e a média foi de: {resultado}')
    print (f"O maior número foi: {max(numero)} e o menor número foi: {min(numero)}")
'''  
    

  
    









   




