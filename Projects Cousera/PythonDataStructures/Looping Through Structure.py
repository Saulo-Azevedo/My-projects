fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count =  count+1
print(count)

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:12])
print('-------')
print(s[:2])
print(s[8:])
print(s[:])

fruit = 'banana'
'n' in fruit
True

'm' in fruit
False

'nam' in fruit
True

if 'a'in fruit :
    print('found it')




