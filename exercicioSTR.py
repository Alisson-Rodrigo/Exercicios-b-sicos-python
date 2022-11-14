"""
Tamanho de strings. 
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""



string1 = str(input("Digite: "))
string2 = str(input("Digite: "))

print (f"'{string1}' o Tamanho da string1 é: {len(string1)}")
print (f"'{string2}' o Tamanho da string1 é: {len(string2)}")

if len(string1) == len(string2):
    print ('As duas strings tem o mesmo comrpimento')
else:    
    print ("Tamanho diferentes")
    

if string1 == string2:
    print ("Tem o mesmo conteúdo")
else:
    print ('Não tem o mesmo conteudo')
    


 