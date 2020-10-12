import turtle
import time
import random
# This program is of making pie chart with the help of inbuilt turtle module, It is one of my first programs in python
# Author : Anant Mishra
# Made in October 2019
t = turtle.Turtle()
p = turtle.Turtle()
t.speed(0)
p.pensize(3)
p.shape("square")
p.up()
p.hideturtle()
src = turtle.Screen()
src.setup(1000, 700)


def home():
    # Home Screen :
    t.hideturtle()
    src.bgcolor("black")
    src.title("Home Screen")
    t.up()
    t.color("orange")
    t.goto(-120, 200)
    t.write("Pie Chart", font=("Arial", 50, "normal"))
    t.goto(-250, 100)
    t.color("green")
    t.write("Project by Anant Mishra :)", font=("Arial", 35, "normal"))
    t.down()
    time.sleep(2)

    pie_chart()

# Taking variables :
def pie_chart():
    src.clearscreen()
    src.title("Pie Chart")
    src.bgcolor("dodger blue")
    n = src.numinput("No. of variables ", "Quantity")
    n = int(n)
    pie = []
    ln = []
    for i in range(0, n):
        b = src.textinput("Name of variable", "Name")
        ln.append(b)
        a = src.numinput("Values of variables", "Value : ")
        a = int(a)
        pie.append(a)

    # Sum of values of variables :
    c = 0
    for i in pie:
        c = c + i

    # Dividing each value by sum :
    pie[0:n] = [i / c for i in pie[0:n]]
    tie = list(pie)

    # Finding angle for each value of variable :
    pie[0:n] = [i * 360 for i in pie[0:n]]

    # Making pie chart :
    def legend(name, colr, x, perc):
        time.sleep(0.2)
        a = round(perc, 4) * 100
        b = str(a) + "  %"
        p.color(colr)
        p.goto(-380, x + 25)
        p.stamp()
        p.goto(-350, x + 10)
        p.color("white")
        p.write(name, font=("Arial", 20, "normal"))
        p.goto(-280, x + 10)
        p.write(b, font=("Arial", 20, "normal"))

    def makepie(ln, tie, pie):
        x = 200
        l1 = ["orange", "green", "cyan", "violet", "yellow", "purple", "red", "pink", "yellow green", "peru", "brown",
              "blue violet", "maroon"]
        t.goto(200, -150)

        for i in range(len(pie)):
            t.begin_fill()
            c = random.choice(l1)
            l1.remove(c)
            t.fillcolor(c)
            t.circle(150, pie[i])
            p = t.pos()
            t.goto(200, 0)
            legend(ln[i], c, x, tie[i])
            t.end_fill()
            t.goto(p)
            x = x - 30

    makepie(ln, tie, pie)


home()

src.mainloop()
