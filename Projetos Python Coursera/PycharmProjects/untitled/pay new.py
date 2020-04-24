hours = input('Enter hours:\n')
rate = input('Enter rate:\n')
pay = float(hours) * float(rate)
if float(hours) <= 40:
    print('normal hours', pay)
elif float(hours) > 40:
    rate_ex = input('enter rate extra:\n')
    ext = (float(hours) - 40)
    pay = ((ext * 10.50) * 0.5) + pay
    print('payment amount', pay)
