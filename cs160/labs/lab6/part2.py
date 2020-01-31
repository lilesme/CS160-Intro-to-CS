def prompt():
    nums=int(input("How many integers would you like to enter?"))
    list=[]
    y=1
    for i in range(nums):
        x=int(input("Number" +str(y)+ ":"))
        if x < 101:
            list.append(x)
        else:
            list.append('over')
        y=y+1
    for j in range(len(list)):
        print(list[j],end="")
        print(" ", end="")
    print("")

def main():
    prompt()


main()
