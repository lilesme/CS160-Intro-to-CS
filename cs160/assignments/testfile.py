def isCorrectLength(l, length):
    
    if l == length:
        return True
    else:
        return False

def get_length():
    length=int(input("Please enter the correct length: "))
    return length


def main():

    s=input("String:")

    l=len(s)
    length=get_length()
    correct=isCorrectLength(l,length)
    print(correct)
    if correct==True:
        print("That is the correct length!")
    else:
        print("That is not the correct length!")


main()
