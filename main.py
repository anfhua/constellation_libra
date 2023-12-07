import time
import turtle

"""

    Constellation Project Libra
    CIS 401 PROJECT 3
    AUTHOR: ANTHONY HUANG
    DATE: 11/09/2023

"""

# Screen SIZE
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creating the screen
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Constellation Project by Anthony Huang")

# Creating the turtle
pen = turtle.Turtle()
pen.hideturtle()


# Function to draw constellation stars
def draw_constellation_stars():
    wn.bgpic("starbackground.gif")
    pen.color("white")
    pen.speed("slow")
    time.sleep(10)  # Wait 10 seconds before drawing stars

    stars = {
        "48": (-95, 35),
        "θ Lib": (-80, 20),
        "Zuben Elgenubi": (-40, 30),
        "Zubenelakrab": (-30, 50),
        "Zubeneschamali": (10, 70),
        "Zubenelgenubi": (60, 30),
        "Zubenelhakrabi": (20, -40),
        "υ Lib": (-30, -50),
        "τ Lib": (-35, -70)
    }

    star_names = list(stars.keys())

    for star, position in stars.items():
        pen.penup()
        pen.goto(position)
        pen.dot(10)  # Draw the star
        pen.write(star, align="left")

    # Define pairs of stars to connect with lines
    star_pairs = [
        ("48", "θ Lib"),
        ("θ Lib", "Zuben Elgenubi"),
        ("Zuben Elgenubi", "Zubenelakrab"),
        ("Zubenelakrab", "Zubeneschamali"),
        ("Zubeneschamali", "Zubenelgenubi"),
        ("Zubenelgenubi", "Zubenelhakrabi"),
        ("Zubenelhakrabi", "υ Lib"),
        ("υ Lib", "τ Lib"),
        ("Zubeneschamali", "Zubenelhakrabi")
    ]

    for star1, star2 in star_pairs:
        pen.penup()
        pen.goto(stars[star1])
        pen.pendown()
        pen.goto(stars[star2])
        pen.penup()


# Splash page
wn.bgpic("project3pg1.gif")


# Page 2
def setBGImage2():
    wn.bgpic("project3pg2.gif")
    wn.ontimer(setBGImage3, 20000)  # Set the next transition after 20 seconds


turtle.ontimer(setBGImage2, 20000)


# Page 3
def setBGImage3():
    wn.bgpic("project3pg3.gif")
    wn.ontimer(draw_constellation_stars, 30000)  # Call the draw stars after 30 seconds


# Start the sequence by transitioning to the second image after 20 seconds
wn.ontimer(setBGImage2, 20000)

# End
wn.exitonclick()
