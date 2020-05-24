fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word= line.rstrip().split()
    for d in word:
        if d in lst:
            continue
        else :
            lst.append(d)
lst.sort()
print (lst)