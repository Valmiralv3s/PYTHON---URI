

a = float(input())
b = float(input())
c = float(input())
# declarando as variaveis de outra forma
# x = input().split()

# a, b, c = x
pi = 3.14159
TRIANGULO = ((float(a) * float(c)) / 2)
CIRCULO = (pi * float(c)**2)
TRAPEZIO = (float(c) * ((float(a) + float(b)) / 2))
QUADRADO = (float(b)**2)
RETANGULO = (float(a) * float(b))

print('TRIANGULO = {:.3f}'.format(TRIANGULO))
print('CIRCULO = {:.3f}'.format(CIRCULO))
print('TRAPEZIO = {:.3f}'.format(TRAPEZIO))
print('QUADRADO = {:.3f}'.format(QUADRADO))
print('RETANGULO = {:.3f}'.format(RETANGULO))
