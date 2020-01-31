dec=int(input("Provide a decimal: "))
a=dec//128
dec=dec-(128*a)
b=dec//64
dec=dec-(64*b)
c=dec//32
dec=dec-(32*c)
d=dec//16
dec=dec-(16*d)
e=dec//8
dec=dec-(8*e)
f=dec//4
dec=dec-(4*f)
g=dec//2
dec=dec-(2*g)
h=dec//1
dec=dec-(1*h)

print(c,b,d,e,f,g,h)

