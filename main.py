import math

exemplo = lambda x:x**3 + 4*(x**2) - 10
a = lambda x:x - 2**(-x)
b = lambda x:math.exp(x)- x**2 + 3*x - 2
c = lambda x:2*x*math.cos(2*x) - (x+1)**2
d = lambda x:x*math.cos(x) - 2*x**2 + 3*x -1

def bissec(f,intervalo,tol,n):
  a = intervalo[0]
  b = intervalo[1]
  fa = f(a)
  i = 1
  print()
  print("-"*91)
  print("| i  |       a     |       b     |       p     |      f(a)    |      f(b)   |      f(p)   |")
  while i<=n:
    p = a + (b-a)/2
    fp = f(p)
    print("| {0}  |   {1:.6f}  |   {2:.6f}  |   {3:.6f}  |   {4:.6f}  |  {5:.6f}  |   {6:.6f}  |".format(i,a,b,p,f(a),f(b),f(p)))
    if(fp == 0 or abs(f(p))<tol):
      return "-"*91+"\nProcedimento concluído com sucesso. P({}) = {}\n".format(i,p)
    i += 1
    if(fa*fp>0):
      a = p
      fa = fp
    else:
      b = p
  return "-"*91+"\nO método falhou após {} iterações\n".format(i)

#exemplo
print(bissec(exemplo,(1,2),0.1,10))

#a
print(bissec(a, (0, 1), 0.00001, 100))

#b
print(bissec(b, (0, 1), 0.00001, 100))

#c
print(bissec(c, (-3, -2), 0.00001, 100))

#c
print(bissec(c, (-1, 0), 0.00001, 100))

#d
print(bissec(d, (0.2, 0.3), 0.00001, 100))

#d
print(bissec(d, (1.2, 1.3), 0.00001, 100))