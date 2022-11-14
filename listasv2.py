'''
lista = []
dado = []
cont = 0

for c in range(0,2):
    dado.append(str(input("Digite um nome: ")))
    dado.append(int(input("Digite o seu peso: ")))
    lista.append(dado[:])
    dado.clear()
    cont += 1
print (f"\nForam cadastradas {cont} pessoas. \n")
print ("Pessoas mais pesadas: ")
for c in lista:
    if c[1] >= 80:
        print (c)      
print ("\nPessoas mais leves: ")    
for c in lista:
    if c[1] < 80:
        print (c)
'''

'''
lista = []
lista2 = []
cont = 0

for i in range (0,3):
    lista2.append(int(input(f"Digite um valor na matriz {[i]}[0]: ")))
    lista2.append(int(input(f"Digite um valor na matriz {[i]}[1]: ")))
    lista2.append(int(input(f"Digite um valor na matriz {[i]}[2]: ")))
    lista.append(lista2[:])
    lista2.clear()
for c in lista:
    print (f"[{lista[cont][0]}]",end='')
    print (f"[{lista[cont][1]}]",end='')
    print (f"[{lista[cont][2]}]",end='')
    print ("")
    cont += 1
'''


'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
aux = []     
soma = 0
somaC = 0


for c in range (0,3):
    for i in range (0,3):
        matriz[c][i] = (int(input(f"Digite um número na posição [{c}][{i}]")))
        if matriz[c][i] % 2 == 0:
            soma += c + i
        if matriz[c][2] == 2:
            somaC += i
        if matriz[1][i] == 1:
            aux.append(c and i)
for c in range(0,3):
    for i in range(0,3):
        print (f"[{matriz[c][i]}]",end='')
    print ("")

print (f"A soma dos números pares: {soma}")
print (f"A soma dos valores na coluna 3 é: {somaC}")
print (f"O maior valor da linha 2 é: {max(aux)}")
'''
    

