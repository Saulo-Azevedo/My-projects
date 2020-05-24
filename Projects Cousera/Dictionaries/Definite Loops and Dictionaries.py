'''
        Definite Loops adn Dictionaries
Even trough dictionaries are not stored in order,
we can wirte a for loop that goes through all the entries in a dictionary -
actually it goes through all of the keys in the dictionary adn loops up the values.

        Definindo Loops e dicionários
Até os dicionários não são armazenados em ordem,
podemos criar um loop for que passa por todas as entradas de um dicionário -
na verdade, ele passa por todas as chaves do dicionário e faz um loop dos valores.
'''

counts = {'Chuck':1,'Fred':42, 'jan':100}
for key in counts:
    print(key,counts[key])
