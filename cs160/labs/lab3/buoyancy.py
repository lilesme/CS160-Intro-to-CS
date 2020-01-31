import math

x=1
while(x==1):
	w=float(input("Provide the weight(lbs): "))
	r=float(input("Provide the radius(feet): "))

	v=(4/3)*(math.pi)*pow(r,3)

	y=62.4
	F=v*y

	if F>=w:
		print("This sphere will float")
	elif F<w:
		print("This sphere will sink")

	
	x=int(input("Again? Yes(1) No(2): "))

