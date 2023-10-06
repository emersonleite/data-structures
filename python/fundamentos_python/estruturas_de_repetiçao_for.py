""" Estruturas de repetição """

""" De 1  5 """
for numero in range(1, 6):
    print(numero)

""" Decrescente """
for numero in range(5, 0, -1):
    print(numero)

""" Fazendo soma """
soma = 0 

for numero in range(1, 6):
    soma = soma + numero

print(soma)


""" Percorrendo uma palavra """
palavra = 'sorvete'
for letra in palavra:
    print(letra)

""" Aninhamento """
for i in range(0, 5):
    print(i)
    print('---')
    for j in range(0, 3):
        print(j)
    print()