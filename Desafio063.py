# fibonacci again
fim = int(input('Digite a quantidade de termos: '))
a = 1
b = 1
c = 0
print(c, end=' ')

while fim - 1 > 0:
    a = b
    b = c
    c = a + b
    print(c, end=' ')
    fim -= 1
