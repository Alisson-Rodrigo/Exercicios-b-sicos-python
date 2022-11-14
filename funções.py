'''
def calculoArea():
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input('Digitew a largura: '))
    area = largura * comprimento
    return area

aux = calculoArea()
print (aux)
'''

from time import sleep

def contador():
    print ("Contagem de 0 até 10 de 1 em 1: ")

    for c in range (0,11,1):
        print (f'{c}',end=' ')
    print ('')
    print ("Contagem de 10 até 0 de 2 em 2: ")
    for c in range (10,0,-2):
        print (f'{c}',end=' ')
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    passo = int (input("Passo: "))
    
    if inicio < fim:
        passo = +passo
        for c in range (inicio,fim,passo):
            print (f'{c}')    




