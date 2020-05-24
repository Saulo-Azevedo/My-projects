def greet(lang):
    if lang == 'es':
        return ("hola")
    elif lang == 'fr':
        return ("Bonjour")
    else:
        return ("hello")


print(greet('en'), 'Glen')
print(greet('es'), 'saly')
print(greet('fr'), "Michael")
