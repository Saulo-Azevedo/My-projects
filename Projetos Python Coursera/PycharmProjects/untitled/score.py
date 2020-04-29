def score(scor)
if scor >= 0.9 and scor < 1.0:
    return("A")
elif scor >= 0.8 and scor < 0.9:
    return("B")
elif scor >= 0.7 and scor < 0.8:
    return("C")
elif scor >= 0.6 and scor < 0.7:
    return("D")
elif scor < 0.6:
    return("F")
else:
    return("Error")

sc = input("enter Score: ")
try:
    fsc = float(sc)
except:
    print("Error")
    quit()

'''def computepay(hours, rate):
    #print("In computepay", hours,rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    #print("Returning", pay)
    return pay

sh = input ("Enter hours: ")
sr = input ("Enter rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay",xp)'''
