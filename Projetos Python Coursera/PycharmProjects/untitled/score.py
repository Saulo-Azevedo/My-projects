score = input("enter Score: ")
try:
    fsc = float(score)
except:
    print("Error")
    quit()

if fsc >= 0.9 and fsc < 1.0:
    print("A")
elif fsc >= 0.8 and fsc < 0.9:
    print("B")
elif fsc >= 0.7 and fsc < 0.8:
    print("C")
elif fsc >= 0.6 and fsc < 0.7:
    print("D")
elif fsc < 0.6:
    print("F")
else:
    print("Error")
