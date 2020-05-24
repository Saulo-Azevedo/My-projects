'''
                      Counting Pattern
The general pattern to count the words in a line of text is to split the line into words,
then loop through the words and use a dictionary to track the count of each word independently.

                    Padrão de contagem
O padrão geral para contar as palavras em uma linha de texto é dividir a linha em palavras,
percorrer as palavras e usar um dicionário para rastrear a contagem de cada palavra independentemente
'''

'''
Using text for exemple
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
'''


counts = dict()
print('Enter a line of text:')
line = input()

words = line.split()

print('Words: ',words)

print("Counting....")
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts: ', counts)