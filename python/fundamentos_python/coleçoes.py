""" ------------------ TUPLAS ------------------------- """

tupla = ('homo sapiens', 'canis familiaris', 'Felis catus' )

print(tupla)


""" Acessando itens """

print(tupla[0])

print(tupla[2])

""" Pegando o index """
print(tupla.index('canis familiaris'))

""" Percorrendo """
for elemento in tupla:
    print(elemento)


""" ------------------ lISTAS ------------------------- """

l1 = ['homo sapiens', 'canis familiaris', 'Felis catus']
l2 = ['xenopus laevis', 'Ailuropoda melanoleuca']

""" Somando listas """
l3 = l1 + l2

print(l3)

""" Multiplicando listas """

l2_2 = l2 * 2 

print(l2_2)

""" Acessando elementos """
print(l1[0])
print(l1[0:2])

""" Adicionanando elementos """
l1.append('Gorila gorila')

print(l1)

""" Removendo elementos """
l1.remove('Felis catus')
print(l1)

""" Apagando a lista inteira """
#del(l1)
print(l1)

""" Percorrendo elementos """
for item in l2_2:
    print(item)


""" ------------------ DICIONÁRIOS ------------------------- """
coleta = {
    'Aeges aegypt' : 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14
}

""" Acessando elementos """
print(coleta['Aeges aegypt'])

""" Adicionando elementos """
coleta['Rhodnius montenegrensis'] = 11

print(coleta)

""" Apagando elementos """
del(coleta)['Aedes albopictus']
print(coleta)

""" Forma de dicionário """
print(coleta.items())

print(coleta.keys())

print(coleta.values())

""" Adicionando um dicionário a outro  """
coleta2 = {"Anopheles gambiae" : 13, 'Anopheles deaneorum' : 14}

coleta.update(coleta2)

print(coleta)

""" Percorrendo elementos """
for especie, num_especimes in coleta.items():
    print(f'espécie: {especie}, número: {num_especimes}')


""" ------------------ CONJUNTOS ------------------------- """
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato','lipídeo', 'ácidos nucleicos', 'carboidrato' , 'carboidrato', 'carboidrato' )

print(biomoleculas)

""" Mostrando elementos únicos """
print(set(biomoleculas))

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}

""" Interseção """
c3 = c1.intersection(c2)

print(c3)

""" Diferença """
print(c1.difference(c2))