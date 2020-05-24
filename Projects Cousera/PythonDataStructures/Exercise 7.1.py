fname = input('Enter file name: ')
fh = open(fname)
inp = fh.read()
inp = inp.rstrip()

print(inp.upper())