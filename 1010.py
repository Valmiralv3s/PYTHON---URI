
# dando err0
a = input().split()
cod1, pec1, valor1 = a
b = input().split()
cod2, pec2, valor2 = b

total = float(int(valor1)*float(pec1)+int(valor2)*float(pec2))

print('Valor a pagar: R$ {:.2f}'.format(total))


# respostas do exercicio

#a = input().split()
#ca, qa, va = a
#b = input().split()
#cb, qb, vb = b

#t = float(int(qa) * float(va) + int(qb) * float(vb))
#print('VALOR A PAGAR: R$ {:.2f}'.format(t))
