""" EXPRESSÕES REGULARES """

import re 

""" Função search """

frase = 'Olá, meu número de telefone é (42)00010-0000'
t = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
print(t)

frase2 = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
t2 = re.search('[A-Za-z]{3}-\d{4}', frase2)
print(t2)


email = 'Entre em contato, meu email é teste@teste.com'
t3 = re.search('\w+@\w+\.com', email)
print(t3)


""" Função match - início do texto """
frase3 = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
t4 = re.match('[A-Za-z]{3}-\d{4}', frase3)
print(t4)

frase4 = 'FRT-1998 é a placa do carro'
t5 = re.match('[A-Za-z]{3}-\d{4}', frase4)
print(t5)

""" Função findall """

frase5 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
t6 = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase5)
print(t6)


emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

t7 = re.findall('\w+@\w+\.\w*',emails)
print(t7)