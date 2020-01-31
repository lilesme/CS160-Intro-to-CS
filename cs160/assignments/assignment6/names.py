def get_num_names():
   num_names=int(input("How many names would you like to enter?"))
   return num_names

def get_names(name_list, num_names):
    for x in range(num_names):
        name=input("Name "+str(x)+":").lower()
        name_list[x]=name

    count(name_list, num_names)


def count(name_list, num_names):
    counter=['0']*26
    for x in range(num_names):
        for y in range(len(name_list[x])):
            if name_list[x][y]=='a':
                counter[0]=int(counter[0])+1
            elif name_list[x][y]=='b':
                counter[1]=int(counter[1])+1
            elif name_list[x][y]=='c':
                counter[2]=int(counter[2])+1
            elif name_list[x][y]=='d':
                counter[3]=int(counter[3])+1
            elif name_list[x][y]=='e':
                counter[4]=int(counter[4])+1
            elif name_list[x][y]=='f':
                counter[5]=int(counter[5])+1
            elif name_list[x][y]=='g':
                counter[6]=int(counter[6])+1
            elif name_list[x][y]=='h':
                counter[7]=int(counter[7])+1
            elif name_list[x][y]=='i':
                counter[8]=int(counter[8])+1
            elif name_list[x][y]=='j':
                counter[9]=int(counter[9])+1
            elif name_list[x][y]=='k':
                counter[10]=int(counter[10])+1
            elif name_list[x][y]=='l':
                counter[11]=int(counter[11])+1
            elif name_list[x][y]=='m':
                counter[12]=int(counter[12])+1
            elif name_list[x][y]=='n':
                counter[13]=int(counter[13])+1
            elif name_list[x][y]=='o':
                counter[14]=int(counter[14])+1
            elif name_list[x][y]=='p':
                counter[15]=int(counter[15])+1
            elif name_list[x][y]=='q':
                counter[16]=int(counter[16])+1
            elif name_list[x][y]=='r':
                counter[17]=int(counter[17])+1
            elif name_list[x][y]=='s':
                counter[18]=int(counter[18])+1
            elif name_list[x][y]=='t':
                counter[19]=int(counter[19])+1
            elif name_list[x][y]=='u':
                counter[20]=int(counter[20])+1
            elif name_list[x][y]=='v':
                counter[21]=int(counter[21])+1
            elif name_list[x][y]=='w':
                counter[22]=int(counter[22])+1
            elif name_list[x][y]=='x':
                counter[23]=int(counter[23])+1
            elif name_list[x][y]=='y':
                counter[24]=int(counter[25])+1
            elif name_list[x][y]=='z':
                counter[25]=int(counter[25])+1

    print_numbers(counter)

def print_numbers(counter):
    n=65
    for x in range(len(counter)):
        if int(counter[x])>0:
            print(chr(n)+ ": "+ str(counter[x]))
        n=n+1


def main():

   num_names=get_num_names()
   name_list=['']*num_names
   get_names(name_list, num_names)


main()
