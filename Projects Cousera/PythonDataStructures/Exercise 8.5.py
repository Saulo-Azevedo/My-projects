fname = input('Enter file name : ')
fhand = open(fname)
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    count += 1
    words = line.split()
    print(words[1])

print('There were',count,'lines in the file with From as the first word')


