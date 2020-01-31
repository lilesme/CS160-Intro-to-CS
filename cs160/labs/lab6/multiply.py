def multiply():
    n=int(input("Enter a positive integer: "))
    i=1
    j=1
    for i in range(n):
        for j in range(n):
            num=i*j
            if num<10:
                space="   "
            elif num<100:
                space="  "
            else:
                space=" "
            print(space, num, end="")
        print()

def main():
    multiply()

main()
