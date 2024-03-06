import turtle

wn = turtle.Screen()
t = turtle.Turtle()

c = input("chose your color :")
t.color(c)

s = float(input("chose your line size :"))


for i in range(4) :
    
    t.forward(s)
    t.right(90)

wn.mainloop()