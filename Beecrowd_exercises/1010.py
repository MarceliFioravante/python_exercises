'''n this problem, the task is to read a code of a product 1,
the number of units of product 1, the price for one unit of product 1,
 the code of a product 2, the number of units of product 2 and the price
  for one unit of product 2. After this, calculate and show the amount to be paid.'''

a, b, c = input().split()
d, e, f = input().split()
a = int(a)
b = int(b)
c = float(c)
d = int(d)
e = int(e)
f = float(f)
amount = (b * c) + (e * f)
print(f'VALOR A PAGAR: R$ {amount:.2f}')
