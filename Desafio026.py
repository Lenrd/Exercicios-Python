frase = str(input('digite uma frase: ')).lower().strip()
print('A quantidade de aparições é: {}'.format(frase.lower().count('a')))
print('A primeira aparição é: {}'.format(frase.lower().find('a')+1))
print('A última aparição é: {}'.format(frase.lower().rfind('a')+1))
