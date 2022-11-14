'''
lanche = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte1')

cont = 0

for c in lanche:
    cont = int(input("Digite um número: "))
    if cont >= 0 and cont <= 20:
        print (f"Você digitou o número: {lanche[cont]}")
        print ("")
    elif cont < 0 and cont > 20:
        print ("Inválido!")
        while cont < 0 and cont > 20:
            cont = int(input ("Digite um número: "))
    elif cont == 999:
        print ("Fim do programa!")
        break
'''


'''
from operator import index

classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 
'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print (f"Lista de times: {classificacao}\n")
print (f"Os 5 primeiros colocados: {classificacao[0:5]})\n")
print (f"Os 4 últimos colocados: {classificacao[-4:]}\n")
print (f"Em ordem alfabetica {sorted(classificacao)}")
chapeco = classificacao.index('Chapecoense') + 1
print (f"Chapecoense está na posição: {chapeco}")
'''

'''
from random import randint

00
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print (numeros)
print (f"O menor: {min(numeros)}")
print (f"O maior: {max(numeros)}")
'''

'''
cont = 0
lista = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))
print (f"\nVocê digitou: {lista}")
for d in lista:
    if d == 9:
        cont+=1
print (f"O número 9 apareceu: {cont}")
print ("Os valores são pares: ", end=' ')
for c in lista:
    if c % 2 == 0: 
        print (f"({c})", end=' ')
print ("")
print (f"O número 3 está na posição: ({lista.index(3) + 1})")
print ("")
'''

'''
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
'''

'''
vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')

for palavra in palavras:

    print(f'Vogais da palavra ({palavra}): ', end='')

    for letra in palavra:

        if letra.lower() in vogais:
            print(f'\033[1;33m{letra.lower()}\033[m', end=' ')

    print()
    
'''





