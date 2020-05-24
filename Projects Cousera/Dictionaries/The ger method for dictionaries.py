'''
                 The get method for dictionaryies.
The pattern of checking to see if a key is already in a dictionary
and assuming a default value if the key is not there is so commom
 that there is a method called get () that does this for us.

               O método get para dicionários.
O padrão de verificar se uma chave já está em um dicionário e assumir
um valor padrão se a chave não estiver lá é tão comum que existe um método
 chamado get () que faz isso por nós.
 '''

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name in counts: #se o nome que estamos vendo não estiver em nosso dicionário, defina count sub name = 1
        x = counts[name]
    else:
        x = 0
    x = counts.get(name,0)
print(counts)