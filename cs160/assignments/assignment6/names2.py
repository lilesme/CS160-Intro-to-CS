def get_num_names():
   num_names=int(input("How many names would you like to enter?"))
   return num_names

def get_names(name_list, num_names):
   for x in range(num_names):
      name=input("Name "+str(x)+":").upper()
      name_list[x]=name
   count(name_list, num_names)


def count(name_list, num_names):
   counter=['0']*26
   for x in range(num_names):
      for y in range(len(name_list[x])):
         letter=int(name_list[x][y])
         counter[letter-65]+=1

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
