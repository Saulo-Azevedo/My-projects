fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
    print (words[3])
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)

email = words[1]
print(email)

pieces =email.split('@')
print(pieces)
print(pieces[0])
print(pieces[1])