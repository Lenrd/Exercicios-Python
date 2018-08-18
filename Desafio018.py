import math
ang = int(input('Digite o angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Os seno, coseno e tangente do angulo {} são: {:.2f}, {:.2f} e {:.2f}'.format(ang, seno, cos, tan))
