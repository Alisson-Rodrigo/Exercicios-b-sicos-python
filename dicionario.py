'''
dicionario =  {'nome':input("Nome: "), 'media':float(input("Media: "))}
print ("")
if dicionario['media'] >= 7:
    print (f"Nome: {dicionario['nome']}")
    print (f"Média: {dicionario['media']}")
    print (f"Situação: Aprovado")
else:
    print (f"Nome: {dicionario['nome']}")
    print (f"Média: {dicionario['media']}")
    print (f"Situação: Reprovado")
'''

'''
from random import randint
from time import sleep

dicionario = {'jogador1':randint(1,6),
              'jogador2':randint(1,6),
              'jogador3':randint(1,6),
              'jogador4':randint(1,6)}

for c, k in dicionario.items():
    print (f'O {c} tirou : {k}')
    sleep(1)
'''
'''
def novoNome (a,b): 
    nomes = {a:b}
    return nomes

aux = input ("Digite seu nome: ")
telofone = int(input("telofone: "))
resultado = novoNome(aux, telofone)
print (resultado)
'''    
