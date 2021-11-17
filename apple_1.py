#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  drawer.color("white")
  drawer.penup()
  drawer.setx(apple.xcor()-18)
  drawer.sety(apple.ycor()-40)
  drawer.write("A", font=("Arial", 45, "bold"))
  wn.update()
def drop_apple():
  apple.penup()
  apple.goto(apple.xcor(),-150)
  drawer.hideturtle()
  drawer.clear()
  apple.hideturtle()

#-----function calls-----
#drop_apple()
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.bgpic("background.gif")
wn.mainloop()