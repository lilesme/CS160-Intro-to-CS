import sys

def count(n,counter, book):
    x=ord(n)

    if (x > 64 and x < 91) or (x > 96 and x < 123):
        #print(x)
        if x > 96:
            index=x-97
        elif x > 64:
            index=x-65


        num=counter[index]
        num=num+1
        counter[index]=num
        num1=book[index]
        num1=num1+1
        book[index]=num1

def print_book(book, i):
    name=sys.argv[i]
    l=open('frequency_results.txt', 'a')
    l.write("\n")
    l.write(name)
    l.write(" : \n")
    n=65
    for x in range(len(book)):
        n=chr(n)
        num=str(book[x])
        l.write(n)
        l.write(": ")
        l.write(num)
        l.write(" ")
        n=ord(n)
        n=n+1
    l.write("\n")
    l.close()

def print_numbers(counter):
    l=open('frequency_results.txt', 'a')
    l.write("\n")
    l.write("OVERALL: \n")
    n=65
    for x in range(len(counter)):
        n=chr(n)
        num=str(counter[x])
        l.write(n)
        l.write(": ")
        l.write(num)
        l.write(" ")
        n=ord(n)
        n=n+1



def main():

    n=len(sys.argv)
    if n != 4:
        print("That is not the correct number of arguments!")
        return
    counter=[0]*26
    for i in range(n):
        book=[0]*26
        try:
            f=open(sys.argv[i], 'r')
        except IOError:
            print("This file does not exist: ", sys.argv[i])
            return


        while 1:
           n=f.read(1)
           if not n: break
           count(n, counter, book)

        print_book(book, i)
    print_numbers(counter)






main()
