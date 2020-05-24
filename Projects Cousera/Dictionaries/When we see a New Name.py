'''
         When we see a new name.
When we counter a new name, we need to add a new entry in the dictionary
and if this the second ou later we have seen the name,
we simply add one to the count in the dictionary under that name.

                Quando vemos um novo nome.
Quando contamos com um novo nome, precisamos adicionar uma nova entrada no dicionário e,
se este for o segundo ou mais tarde, vimos o nome, simplesmente adicionamos um à
contagem no dicionário sob esse nome.
Código com traceback.
'''

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)