nome = str(input('Digite seu nome: ')).lower().strip()
ver = nome.lower().find('silva')
print('tem silva no nome? {}'.format(ver != -1))
