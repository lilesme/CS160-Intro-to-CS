def fruit(fruit_list, num_fruits, weight_list):
    for i in range(num_fruits):
        name=input("Fruit name: ")
        fruit_list.insert(i,name)
        weight(num_fruits, weight_list, i)


def get_num_fruits():
    num_fruits=int(input("How many fruits?"))
    return num_fruits

def weight(num_fruits, weight_list, i):
        weight=int(input("Integer weight:"))
        weight_list.insert(i,weight)

def print_list(num_fruits, fruit_list, weight_list):
    for i in range(num_fruits):
        print(fruit_list[i] + ", " + str(weight_list[i]))

def sort_list(num_fruits,fruit_list):
    for i in range(num_fruits):
        for j in range(num_fruits-1):
            for c in range(len(fruit_list[j])):
                if fruit_list[j][c] > fruit_list[j+1][c]:
                    temp=fruit_list[j]
                    fruit_list[j]=fruit_list[j+1]
                    fruit_list[j+1]=temp
    print_list(num_fruits,fruit_list, weight_list)

def main():
    num_fruits=get_num_fruits()
    weight_list=[]*num_fruits
    fruit_list=[]*num_fruits
    fruit(fruit_list,num_fruits, weight_list)
    #sort_list(num_fruits, fruit_list)
    print_list(num_fruits,fruit_list, weight_list)

main()
