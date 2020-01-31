def sort(string):
    l=list(string)
    length=len(string)
    """index=0
    length=len(string)-1
    sorted_list=[]*length
    for i in range(length+1):
        while index < length:
            if unsorted_list[index] < unsorted_list[index+1]:
                max=unsorted_list[index]
                index=index+1
            elif unsorted_list[index+1] < unsorted_list[index]:
                max=unsorted_list[index+1]
                index=index+1
        sorted_list.append(max)"""
        #remove the max letter here
    for i in range(length):
        for j in range(length-1):
            if l[j] > l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp



    print(l)

def main():
    string=input("Enter a string:")
    sort(string)




main()
