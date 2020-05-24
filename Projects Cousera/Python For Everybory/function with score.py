def score(scor):
    if scor >= 0.9 and scor < 1.0:
        return ("A")
    elif scor >= 0.8 and scor < 0.9:
        return ("B")
    elif scor >= 0.7 and scor < 0.8:
        return ("C")
    elif scor >= 0.6 and scor < 0.7:
        return ("D")
    elif scor < 0.6:
        return ("F")
    else:
        return ("Error")


sc = input("enter Score: ")
try:
    fc = float(sc)
    sr = score(fc)
    print(sr)
except:
    print("Error")
    quit()
