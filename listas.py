
'''
from turtle import position

numero = []
insert = 0
posiçãoMax = []
posiçãoMIn = []
insert2 = []

for c in range(0,5):
    insert = int(input("Digite um número: "))
    numero.append(insert)
for posicao, valores in enumerate(numero):
    if valores == max(numero):
        posiçãoMax.append(posicao)
    if valores == min(numero):
        posiçãoMIn.append(posicao)
         
print (f'Você digitou os valores: {numero}')
print (f"O maior valor foi {max(numero)} na posição {posiçãoMax}")
print (f"O menor valor foi {min(numero)} na posição {posiçãoMIn}")
'''

