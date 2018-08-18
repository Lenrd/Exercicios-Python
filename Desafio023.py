# Desafio da unidade dezena e centena
seq = int(input('Digite a sequencia de numeros: '))
u = seq // 1 % 10
d = seq // 10 % 10
c = seq // 100 % 10
m = seq // 1000 % 10
print('{:7}: {}'.format('unidade', u))
print('{:7}: {}'.format('dezena', d))
print('{:7}: {}'.format('centena', c))
print('{:7}: {}'.format('milhar', m))
