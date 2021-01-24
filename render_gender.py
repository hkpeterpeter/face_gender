import turtle
from threading import Timer
import random

male_turtle = ""
female_turtle = "" 
text_turtle = ""

def visualize_init():
    global male_turtle, female_turtle, text_turtle
    turtle.setup(800, 200)
    turtle.title("Gender Display")
    turtle.addshape("icon_male.gif")
    turtle.addshape("icon_female.gif")
    turtle.tracer(False)
    male_turtle = turtle.Turtle()
    female_turtle = turtle.Turtle()
    male_turtle.shape("icon_male.gif")
    female_turtle.shape("icon_female.gif")
    male_turtle.up()
    female_turtle.up()
    text_turtle = turtle.Turtle()
    text_turtle.up()
    text_turtle.hideturtle()

def visualize_done():
    turtle.done()


def visualize(count_man, count_woman):
    global male_turtle, female_turtle, text_turtle
    #turtle.screensize(800, 200)
    turtle.tracer(False)

    text_turtle.clear()
    
    male_turtle.goto(-300, 0)
    female_turtle.goto(300, 0)
    

    my_font = ("Arial", 48, "bold")
    
    
    text_turtle.goto(-250, -25)
    text_turtle.write(str(count_man), font=my_font)
    text_turtle.goto(200, -25)
    text_turtle.write(str(count_woman), font=my_font )

    turtle.tracer(True)

WAIT_SECONDS = 1
def update_display():
    count_man = random.randint(5, 10)
    count_woman = random.randint(5, 10)
    visualize(count_man, count_woman)
    Timer(WAIT_SECONDS, update_display).start()
    

if __name__ == '__main__':
    #count_man, count_woman = 5, 10
    #print("man:", count_man, "woman:", count_woman )
    #visualize(count_man, count_woman)
    visualize_init()
    update_display()
    visualize_done()