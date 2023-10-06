palavra = 'casaco'

print(palavra)

maiuscula = palavra.upper()

print(maiuscula)

minuscula = palavra.lower()

print(minuscula)

capital = palavra.capitalize()

print(capital)


""" Não inclui o índice 3 """
metade_palavra = palavra[0:3]

print(metade_palavra)

ultimas_letras = palavra[3:]

print(ultimas_letras)

palavra2 = palavra.replace('aco', 'inha')

print(palavra)
print(palavra2)

""" find """
print(palavra.find('s'))

""" len """
e = len(palavra)

print(e)

""" Remover espaços em brancos antes e depois """

palavra3 = 'Casaco '

palavra4 = palavra3.strip()

print(palavra4)


""" Acessando variáveis em strings, f para formatar """

n1 = 14
n2 = 16


print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')

