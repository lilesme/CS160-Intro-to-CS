import random

def set_parameters():

    length=int(input("How long would you like the password to be? "))
    special_chars=input("Please enter all of the special characters that can be used: ")
    chars=list(special_chars)
    capitals=int(input("How many capital letters would you like? "))

    generate_password(length, chars, capitals)


def generate_password(length, chars, capitals):
    password=""
    counter=0
    for i in range(length):
        #call random option (0-number 1-character, 2-capital)

        if counter==capitals:
            option=random.randint(0,1)
        else:
            option=random.randint(0,2)

        if option==0:
            #generate a number
            x=random.randint(0,9)
            password=password + str(x)

        elif option==1:
            #generate special character
            #get length of the special character list
            l=len(chars)-1
            #get randum number within that length
            index=random.randint(0,l)
            #get special character
            x=chars[index]
            password=password + str(x)

        elif option==2:
            #generate a capital letters
            #random number within capital letter range
            num=random.randint(65, 90)
            #chr(x) change it to a letters
            x=chr(num)
            counter=counter+1
            password=password + str(x)



    #check if there are enough capitals:
    password=list(password)
    #get the last index of the list
    t=len(password)-1
    while counter <= capitals:
        #get a capital letter
        num=random.randint(65, 90)
        #change it to a capital letter
        x=chr(num)
        #add the new capital on the end
        password[t]= str(x)
        #update how many capitals are in the list
        counter=counter+1
        #get the next to last index
        t=t-1


    str(password)
    print("Password:", end="")
    for g in range(len(password)):
        print(password[g], end="")
    print("")


def main():

    set_parameters()



main()
                                                                                                        
