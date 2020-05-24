texto = 'Hoje visitei a velha estação de trem.' \
        ' A estação estava coberta de abandono. ' \
        'Porque, hoje, as pessoas parecem não dar bola para construções velhas' \
        ' como essa da estação de trem. Muitas pessoas só querem saber de coisas futuras.' \
        ' Dão bola só para coisas novas.'
cc  = input ('Informe a palavra ou letra a ser contada:\n')
bb = texto.count(cc)
print('encontramos ',bb,'repetições da palavra ou letra ',cc)