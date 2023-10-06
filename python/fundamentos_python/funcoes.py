""" FUNÇÕES """

""" Sem parâmetro e sem retorno """
def mensagem():
    print('Texto da função')

mensagem()

""" Com parametro """
def mensagem2(texto):
    print(texto)

mensagem2('olá')

""" Com retorno """
def soma(a, b):
    """ Doc da função """
    return a + b

sum = soma(1,2)

print(sum)

""" Mostrando a documentação """
print(help(soma))

