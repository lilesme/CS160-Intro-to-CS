######################################################################

def isPositive(s):
    #checks if a string is a positive integer
    for i in range(len(s)):
        if s[i] < chr(48) and s[i] > chr(57):
            return False
            if s[0]=='-':
                return False

    return True

######################################################################

def isDecimal(s):
   #checks whether a string is a float or double
   for i in range(len(s)):
       if s[i]=='.':
           return True

   return False

######################################################################

def inBound(i, max_val):
    #checks if value x in in the bound of max value
    if i<=max_val:
        return True
    return False

######################################################################

def capitalsPresent(s):
   #checks if the provided string contains a capital
   for i in range(len(s)):
       if chr(64) < s[i] < chr(90):
           return True
       else:
           return False

######################################################################

def numbersPresent(s):
   #checks if provided string contains a number
   for i in range(len(s)):
       if chr(47) < s[i] < chr(58):
           return True
       else:
           return False

######################################################################

def isEven(s):
   #check if integer is even
   positive=isPositive(s)
   decimal=isDecimal(s)
   if positive==True and decimal==False:
       i=int(s)
       if i%2==0:
           return True
       else:
           return False

######################################################################

def isOdd(s):
   #check if string is a positive odd integer
   positive=isPositive(s)
   decimal=isDecimal(s)
   if positive==True and decimal==False:
       i=int(s)
       if i%2!=0:
           return True
       else:
           return False

######################################################################

def isCorrectLength(l, length):
    #indicationg whether a string is the correct length
    if l == length:
        return True
    else:
        return False

######################################################################

def get_string():
    s=input("Please enter a string: ")
    return s;

######################################################################

def get_length():
    length=int(input("Please enter the correct length: "))
    return length

######################################################################

def get_position():
    position=input("Please enter the x or y position: ")
    return position

######################################################################

def get_bound():
    bound=input("Please enter the max bound for the x or y position: ")
    return bound

######################################################################

def main():
    s=get_string()
    #########################
    #is positive
    pos=isPositive(s)
    if pos==True:
        print("That is a positive integer!")
    else:
        print("That is not a positive integer!")
    #########################
    #is decimal
    d=isDecimal(s)
    if d==True:
        print("That is a decimal!")
    else:
        print("That is not a decimal!")
    #########################
    #is a capital letter present
    capital=capitalsPresent(s)
    if capital==True:
        print("There is a capital letter present!")
    else:
        print("There are no capital letters present!")
    #########################
    #is a number present
    number=numbersPresent(s)
    if number==True:
        print("There is a number present!")
    else:
        print("There are no numbers present!")
    #########################
    #is even
    even=isEven(s)
    if even==True:
        print("That is an even integer!")
    else:
        print("That is not an even integer!")
    #########################
    #is odd
    odd=isOdd(s)
    if odd==True:
        print("That is an odd integer!")
    else:
        print("That is not an odd integer!")
    #########################
    #inbound
    position=get_position()
    bound=get_bound()
    in_bounds=inBound(position, bound)
    if in_bounds==True:
        print("That is in bounds!")
    else:
        print("That is out of bounds!")
    #########################
    #correct length
    l=len(s)
    length=get_length()
    correct=isCorrectLength(l,length)
    if correct==True:
        print("That is the correct length!")
    else:
        print("That is not the correct length!")

######################################################################

main()
