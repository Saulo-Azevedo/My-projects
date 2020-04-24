hours = input('Informe as horas :\n')
rate = input('Informe a taxa:\n')
try:
    istr = int(hours)
    istr = int (rate)
    pay = float(hours) * float(rate)
    if float(hours) <= 40:
        print('horas extras normais', pay)
    elif float(hours) > 40:
        rate_ex = input('Informe a taxa extra:\n')
        ext = (float(hours) - 40)
        pay = ((ext * 10) * 0.5) + pay
        print('Valor do pagamento', pay)
except:
    istr = -1
    print('Erro, por favor utiliza uma entrada numerica')


