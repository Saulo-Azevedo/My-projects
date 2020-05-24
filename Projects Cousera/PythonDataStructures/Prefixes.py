line = "Please have a nice day"
# This takes a parameter, what prefix we're looking for.
line_new = line.startswith('Please')
print(line_new)
#Does it start with a lowercase p?
# And then we get back a False because,
# no, it doesn't start with a lowercase p
line_new = line.startswith('p')
print(line_new)

