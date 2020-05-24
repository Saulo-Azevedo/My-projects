text = 'x-DSPAM-Confidence: 0.8475'
atpos = text.find('0')
fatpos = float(atpos)
sppos = text.find('5',atpos)
fsppos = float(sppos)
host = text[atpos:sppos+1]
print(host)






