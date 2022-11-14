'''
import time 

n = int(input ()

for c in range (10,0,-1):
    print (c)
    time.sleep(1) 
'''

'''
for c in range (1,50):
    if c % 2 == 0:
        print (c)
'''

'''
for c in range (1,500):
    if c % 2 == 1:
        if c % 3 == 0:
            print (c)
'''

'''
n = int (input("Digite um número: "))

print ("\tTABUADA\t")
for c in range (1,n):
    print (f"{c} x {n} = {c * n}")
'''

'''
soma = 0

for c in range (1,7):
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        soma += numero
print (soma)
'''

'''
termo1 = int(input("Digite um número: "))
razao = int(input("Digite um número: "))
decimo = termo1 + (10-1) * razao
 

for c in range (termo1,decimo + razao,razao):
    print (f"{c}",end=' --> ')
print ("ACABOU")
'''   

'''
frase = input ("Str: ").strip().upper()
frase = frase.split() 
junto = ''.join(frase)
inverso = ''

for c in range (len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]
if junto == inverso:
    print ('é um palindromo')
else:
    print ('Não é um palindromo')
'''

'''
maior = 0
menor = 0

for c in range (0,7,1):
    idade = int(input ("Digite o ano que você NASCEU: "))
    if idade < 2004:
        maior = maior + 1
    else:
        menor = menor + 1
print (f"As pessoas maiores de 18: {maior}")
print (f"As pessoas menores de 18 {menor}")
'''

'''
lista = []

for c in range (1,6,1):
    pesos = int(input("Digite seu peso: "))
    lista = lista + [pesos]  
print (max(lista))
print (min(lista))
'''

'''
mediaIdade = 0
mais_idade = 0
contF= 0
contM = 0
soma = 0
lista = []


for c in range (1,4,1):
    print (f"\tCadastro pessoa {c}\t\n")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input ("Digite 'M' ou 'F': ").strip().upper()
    
    soma += idade 
    lista += [idade]
    
    if sexo == 'M':
        contM += 1
    if sexo == 'F':
        contF += 1
    
        
    print ("")
    
soma = soma    
mediaIdade = soma / c
        

print (f"A média é igual a: {mediaIdade}")
print (f"A idade mais velha é: {max(lista)}")
print (f"O número de MENINAS é: {contF}")
print (f"O número de MENINOS é: {contM}")
'''


