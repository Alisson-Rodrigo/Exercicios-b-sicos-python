'''
n = s = c = 0

while n != 999:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    c+=1
print (f"O programa executou: {c}")
print (f"O resultado da soma: {s}")

'''

'''
n = 0
nome = 'TABUADA'

while n > -1:
    print (f"{nome:-^20}")
    n = int(input("Digite um valor: "))
    print ("")
    for c in range(1,11,1):
        print (f" {n} x {c} = {n * c}")
    print ("")
'''


'''
from random import randint
print ('\tVAMOS JOGAR PAR OU ÍMPAR\t')
cont = 0

while True: 
    valor_usuario = int(input ("Digite um número: "))
    condição_usuario = input ('Par ou Ímpar: [P/I]: ').upper().strip()
    print ("")
    valor_computador = randint(1,10)
    verificaçao = valor_usuario + valor_computador

    if condição_usuario == 'P':
        if verificaçao % 2 == 0:
            print (f"O resultado foi [{verificaçao}]")
            print (f"Você venceu!")
            print ('')
        elif verificaçao % 2 == 1:
            print (f"O resultado foi: {verificaçao}")
            print (f"Você perdeu! Você teve {cont} WINS")
            break
    if condição_usuario == 'I':
        if verificaçao % 2 == 1:
            print (f"O resultado foi {verificaçao}")
            print (f"Você venceu!")
            print ('')
        elif verificaçao % 2 == 0:
            print (f"O resultado foi: {verificaçao}")
            print (f"Você perdeu! YOU: {cont} WINS" )
            break
    cont += 1
    
'''

'''
contador_maioridade = contador_homens = contador_mulheres_mais20 = 0

while True:
    print('\033[;36m-\033[m' * 30)
    print('     \033[1;97mCADASTRE UMA PESSOA')
    print('\033[;36m-\033[m' * 30)

    idade = int(input('\033[1;97mIdade:\033[m '))
    while True:
        sexo = str(input('\033[1;97mSexo [M/F]:\033[m ')).strip().upper()
        if sexo not in 'MF':
            print('\033[;31mOpção Inválida! Tente de novo.\033[m')
        else:
            break

        if idade >= 18:
            contador_maioridade += 1
        if sexo == 'M':
            contador_homens += 1
        if sexo == 'F' and idade < 20:
            contador_mulheres_mais20 += 1

        continuar = 'S'
        while continuar not in 'SN':
            continuar = str(input('\033[1;97mQuer continuar? [S/N]:\033[m ')).strip().upper()
            if continuar not in 'SN':
                print('\033[;31mOpção Inválida! Tente de novo.\033[m')
            if continuar == 'N':
                break

print('-'*30)
print(f'Total com +18: {contador_maioridade}')
print(f'Total de homens: {contador_homens}')
print(f'Total de mulheres com menos de 20 anos: {contador_mulheres_mais20}')
print('-'*30)

'''


'''
from ast import Break
from time import sleep

print ("\t LOJÃO SUPER BARATO\n")
lista = []
total = 0
cont = 0

while True:
    produto = str(input("Digite o produto desejado: "))
    print ("Cadastrando...")
    sleep(2)
    preço = int(input('Informe o preço do produto: '))
    print ("Cadastrando...")
    sleep (2)
    opção = input("Deseha continuar? ").upper().strip()
    
    while opção not in 'SN':
        opção = input ('Deseja continuar? ').upper().strip()
    if opção == 'S':
        pass
    
    print ("")
    total += preço
    if preço > 1000:
        cont += 1
    lista.append(preço)
    
    if opção == 'N':
        break
    
print ("\t\nRESULTADO\n")        
print (f"Valor total: {total}")
print (f"VOcê comprou {cont} acima de [1000]")
print (f"O produto mais barato foi: {min(lista)}")

'''


print('-'*30)
print('{:^30}' .format(' BANCO ATENA '))
print('-'*30)
d = int(input('Qual valor você quer sacar? R$'))
cont_cinquenta = cont_vinte = cont_dez = cont_um = 0
while True:
    while d - 50 >= 0:
        d -= 50
        cont_cinquenta += 1
    while d - 20 >= 0:
        d -= 20
        cont_vinte += 1
    while d - 10 >= 0:
        d -= 10
        cont_dez += 1
    while d - 1 >= 0:
        d -= 1
        cont_um += 1
    break
if cont_cinquenta != 0:
    print(f'Total de {cont_cinquenta} cedulas de R$50')
if cont_vinte != 0:
    print(f'Total de {cont_vinte} cedulas de R$20')
if cont_dez != 0:
    print(f'Total de {cont_dez} cedulas de R$10')
if cont_um != 0:
    print(f'Total de {cont_um} cedulas de R$1')
    


    

    


    
    


