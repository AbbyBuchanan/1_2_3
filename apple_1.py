#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

#apple = trtl.Turtle()
#drawer = trtl.Turtle()

letters = ["K", "A", "T", "E", "L", "Y", "N", "S"]

apple_list = []
apple_letters = []

for i in range (5):
  apple_list.append(trtl.Turtle())
  apple_letters.append(rand.choice(letters))
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  apple_list[index].penup()
  apple_list[index].shape(apple_image)
  wn.tracer(False)
  apple_list[index].setx(rand.randint(-150,150))
  apple_list[index].sety(rand.randint(-15,100))
  apple_list[index].sety(apple_list[index].ycor()-30)
  apple_list[index].color("white")
  apple_list[index].write(apple_letters[index], align = "center", font=("Arial", 35, "bold"))
  apple_list[index].sety(apple_list[index].ycor()+30)
  apple_list[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()

def typedK():
  for i in range (5):
   if apple_letters[i] == "K":
    drop_apple(i)

def typedA():
  for i in range (5):
   if apple_letters[i] == "A":
    drop_apple(i)

def typedT():
  for i in range (5):
    if apple_letters[i] == "T":
      drop_apple(i)

def typedE():
  for i in range (5):
   if apple_letters[i] == "E":
    drop_apple(i)

def typedL():
  for i in range (5):
   if apple_letters[i] == "L":
    drop_apple(i)

def typedY():
  for i in range (5):
   if apple_letters[i] == "Y":
    drop_apple(i)

def typedN():
  for i in range (5):
   if apple_letters[i] == "N":
    drop_apple(i)

def typedS():
  for i in range (5):
   if apple_letters[i] == "S":
    drop_apple(i)

#-----function calls-----
for i in range (5):
  draw_apple(i)

wn.onkeypress(typedK, "k")
wn.onkeypress(typedA, "a")
wn.onkeypress(typedT, "t")
wn.onkeypress(typedE, "e")
wn.onkeypress(typedL, "l")
wn.onkeypress(typedY, "y")
wn.onkeypress(typedN, "n")
wn.onkeypress(typedS, "s")
wn.listen()

wn.mainloop()