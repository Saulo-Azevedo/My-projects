'''
          Simplified Counting  with get().
We can  use get() and provide a default value of zero when the key
is not yet in the dictionary - and the just add one.

              Contagem simplificada com get ().
Podemos usar get () e fornecer um valor padrão zero quando a chave ainda
 não estiver no dicionário - e apenas adicionar um.
'''

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names :
    counts[name] = counts.get(name,0) +1
print(counts)