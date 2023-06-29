""" MANIPULAÇÃO DE ARQUIVOS """

""" Lendo """
with open('/home/emersonleite/Projects/Projetos pessoais/___data-structures/fundamentos_python/frases.txt') as tex:
    for linha in tex:
        print(linha)

""" Copiando em variável """
with open('/home/emersonleite/Projects/Projetos pessoais/___data-structures/fundamentos_python/frases.txt') as tex:
    r = tex.readlines()

print(r)

""" Escrevendo """
with open('/home/emersonleite/Projects/Projetos pessoais/___data-structures/fundamentos_python/texto2.txt','w') as texto:
    texto.write('Ola mundo de bobocas')

""" Lendo recém criado """
""" 'r' é opcional """
with open('/home/emersonleite/Projects/Projetos pessoais/___data-structures/fundamentos_python/texto2.txt', 'r') as tex:
    for linha in tex:
        print(linha)