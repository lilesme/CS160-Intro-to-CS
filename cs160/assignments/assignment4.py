def calculator():
   choice=input("Subtract(1), Add(2), Multiply(3), Divide(4) or Exponent(5): ")

   num1=float(input("Operand 1: "))

   num2=float(input("Operand 2: "))

   if choice=='1':
      total= num1-num2
      print(total)

   elif choice=='2':
      total= num1+num2
      print(total)

   elif choice=='3':
      total= num1*num2
      print(total)

   elif choice=='4':
      total= num1/num2
      print(total)

   elif choice=='5':
      total= num1**num2
      print(total)


def programmer(dec):
    dec=int(dec)
    binary=''
    while(dec > 0):
        #print("in the while loop")
        remainder = dec % 2
        #print("made it")
        dec=dec//2
        binary += str(remainder)
    print(binary[::-1])





def main():
    again=True
    while again==True:
        a=int(input("Calculator(1) or Programmer(2) or Quit(3): "))
        if a==1:
            calculator()
        elif a==2:
            dec=input("Enter Decimal: ")
            if dec > '0':
                programmer(dec)
            elif dec <= '0':
                print("That is not a good input!")
        elif a==3:
            again=False
        else:
            print("Bad input!")


main()
