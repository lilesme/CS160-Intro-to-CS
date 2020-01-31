import turtle #bring in the turtle library
window = turtle.Screen() #create a variable for the window
megan = turtle.Turtle() #create a variable for your turtle

def reset(x, y):
   megan.reset()

def star(x, y):
   #draw a star
   megan.clear()
   for x in range(5):
      megan.forward(100)
      megan.right(144)

def space():
   megan.left(90)
   megan.penup()
   megan.forward(50)
   megan.pendown()

def m():
   #M
   megan.left(90)
   megan.forward(100)
   megan.right(135)
   megan.forward(71)
   megan.left(90)
   megan.forward(71)
   megan.right(135)
   megan.forward(100)

def e():
   #E
   megan.forward(100)
   megan.left(180)
   megan.forward(100)
   megan.right(90)
   megan.forward(50)
   megan.right(90)
   megan.forward(50)
   megan.left(180)
   megan.forward(50)
   megan.right(90)
   megan.forward(50)
   megan.right(90)
   megan.forward(100)
   megan.right(90)
   megan.penup()
   megan.forward(100)

def g():
   #G
   megan.penup()
   megan.forward(50)
   megan.left(90)
   megan.forward(50)
   megan.pendown()
   megan.right(90)
   megan.forward(50)
   megan.right(90)
   megan.forward(50)
   megan.right(90)
   megan.forward(100)
   megan.right(90)
   megan.forward(100)
   megan.right(90)
   megan.forward(100)
   megan.right(90)
   megan.penup()
   megan.forward(50)
   megan.pendown()
   megan.forward(50)

def a():
   #A
   megan.left(90)
   megan.forward(100)
   megan.right(90)
   megan.forward(100)
   megan.right(90)
   megan.forward(50)
   megan.right(90)
   megan.forward(100)
   megan.right(180)
   megan.forward(100)
   megan.right(90)
   megan.forward(50)

def n():
   #N
   megan.left(90)
   megan.forward(100)
   megan.right(135)
   megan.forward(141.4)
   megan.left(135)
   megan.forward(100)
   megan.right(180)
   megan.forward(100)

def name(x, y):
   megan.reset()
   #go to the left of the screen
   megan.left(180)
   megan.penup()
   megan.forward(500)
   megan.right(180)
   megan.pendown()
   #draw my name
   m()
   space()
   e()
   space()
   g()
   space()
   a()
   space()
   n()

def main():
   again=True
   while(again==True):
       option = int(input("Would you like to see a star(1) or my name(2): "))
       if option == 1:
           megan.onclick(star)
           again=False
       elif option == 2:
           #draw my name
           megan.onclick(name)
           again=False
       else:
           print("Bad Input!")
           again=True
main()
window.mainloop() #wait for the user to close the window
