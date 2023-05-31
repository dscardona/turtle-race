from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

blue = Turtle(shape="turtle")
blue.penup()
blue.goto(x=-230, y=70)
blue.color("blue")

green = Turtle(shape="turtle")
green.penup()
green.goto(x=-230, y=30)
green.color("green")

yellow = Turtle(shape="turtle")
yellow.penup()
yellow.goto(x=-230, y=-10)
yellow.color("yellow")

orange = Turtle(shape="turtle")
orange.penup()
orange.goto(x=-230, y=-50)
orange.color("orange")

red = Turtle(shape="turtle")
red.penup()
red.goto(x=-230, y=-90)
red.color("red")
 
screen.exitonclick()