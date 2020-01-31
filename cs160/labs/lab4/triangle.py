nums=(input("Enter numbers of stars: "))
print(str(nums))
try:
  variable=int(nums)

except ValueError:
   print("This is not a int!")
   quit()
nums=int(nums)
if((nums%2)==0):
  print("That's an even number!")
  quit()

if(nums<0):
   print("Thats not a positive number!")
   quit()
x=1
s=nums-x
while(x<=nums):	
	#print(str(x), str(nums), str(s))
	for y in range(s//2):
		print(" ", end="")
	for i in range(x):
		print("*", end="")
	for q in range(s//2):
	   	print(" ", end="")
	print("") #print new line
	x=x+2
	s=s-2

