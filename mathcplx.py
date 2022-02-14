import math
import vectores as ls

#De pares ordenados a numeros complejos
def prettyPrinting(c):
	print(str(c[0])+'+'+str(c[1])+'i')

#Suma algebraica de complejos
def sumacplx(a,b):
	real=(a[0]+b[0])
	img=(a[1]+b[1])
	return (real,img)

#Multiplicación algebraica de complejos
def multcplx(a,b):
	real=(a[0]*b[0])-(a[1]*b[1])
	img=(a[0]*b[1])+(a[1]*b[0])
	return (real,img)

#Divición algebraica de complejos
def divcplx(a,b):
	real=((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
	img=((b[0]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))
	return (real,img)

#Modulo
def modcplx(a):
	return math.sqrt((a[0]**2)+(a[1]**2))

#Conjugado
def conjcplx(c):
	return str(c[0])+'+'+str(-1*c[1])+'i'

#De polar a cartesiano
def polar_cartcplx(a):
	real=a[0]*math.cos(a[1])
	img=a[0]*math.sin(a[1])
	return (real,img)

#De cartesiano a polar
def cart_polarcplx(a):
	p=modcplx(a)
	if a[0]<0 and a[1]>0:
		theta=math.atan(a[1]/a[0])+math.pi
	if a[0]<0 and a[1]<1:
		theta=math.atan(a[1]/a[0])+math.pi
	if a[0]>0 and a[1]<0:
		theta=math.atan(a[1]/a[0])+2*math.pi
	return (p,theta)

#prettyPrinting(sumacplx((3,-1),(1,4)))
#prettyPrinting(multcplx((3,-1),(1,4)))
#prettyPrinting((divcplx((-2,1),(1,2))))
#print(modcplx((-1,-1)))
#print(conjcplx((-1,-1)))
#print(polar_cartcplx((1,2)))
#print(cart_polarcplx((-1,1)))
#print(cart_polarcplx((1,-1)))

