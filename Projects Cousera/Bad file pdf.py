fname = input('Digite o nome de arquivo: ')
try:
    fhand = open(fname)
except:
    print('Erro informe o nome do arq. correto!',fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Exercícios:'):
        count = count + 1
print('contagem das linhas: ',count,'aqui',fname)
