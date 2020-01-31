def get_lists():
    list1=input("Enter a list of numbers: ")
    list2=input("Enter another list of numbers: ")

    list(list1)
    list(list2)

    get_length(list1, list2)

def get_length(list1, list2):

    length1=len(list1)
    length2=len(list2)

    if length1==length2:
        print("Same Length: Yes | ", end="")

    else:
        print("Same Length: No | ", end="")

    get_sum(list1, list2)

def get_sum(list1, list2):
    sum1=0
    sum2=0
    for x in range(len(list1)):
        sum1=sum1+int(list1[x])

    for y in range(len(list2)):
        sum2=sum2+int(list2[y])

    if sum1==sum2:
        print("Same Sum: Yes ", end="")
    else:
        print("Same Sum: No ", end="")

    print("List 1: " +str(sum1), end="")
    print(" List 2: " +str(sum2)+ " | ", end="")

    get_common_numbers(list1, list2)

def get_common_numbers(list1, list2):
    length1=len(list1)
    length2=len(list2)

    common_numbers=[]

    for x in range(length1):
        for y in range(length2):
            if list1[x]==list2[y]:
                common_numbers.append(list1[x])
    if len(common_numbers)>0:
        print("Common Numbers: Yes- ", end="")
        for i in range(len(common_numbers)):
            print(common_numbers[i], end="")
            print(", ", end="")
        print('')
    else:
        print("Common Numbers: No")

def main():
    get_lists()

main()
