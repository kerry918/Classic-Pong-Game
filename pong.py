# Classic Pong Game by Kerry Liu

import turtle #could do some basic graphics

# Create a window for the game
win = turtle.Screen()
win.title("Pong game by Kerry Liu") #Create a title for the game
win.bgcolor("black") # Change the background color
win.setup(width=800, height=600) # Set up the dimensions of the window
win.tracer(0) # Stops the window from updating to speed up the game


# Main game loop
while True:
    
