# Classic Pong Game by Kerry Liu

# could do some basic graphics
import turtle
import winsound  # module for the sound

# Create a window for the game
win = turtle.Screen()
win.title("Pong game by Kerry Liu")  # Create a title for the game
win.bgcolor("black")  # Change the background color
win.setup(width=800, height=600)  # Set up the dimensions of the window
win.tracer(0)  # Stops the window from updating to speed up the game

# Score
score_a = 0
score_b = 0

# Paddle A
# turtle object, small t is the module name and capital T is the class name
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, set the speed to the maximum possible speed
paddle_a.shape("square")  # set the shape of the paddle
paddle_a.color("white")  # give a color for the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # change the dimension of the paddle using the stretch function
paddle_a.penup()
# since turtle module original is drawing a shape, but there is no need in this game
# so pen up
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation, set the speed to the maximum possible speed
paddle_b.shape("square")  # set the shape of the paddle
paddle_b.color("white")  # give a color for the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # change the dimension of the paddle using the stretch function
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation, set the speed to the maximum possible speed
ball.shape("square")  # set the shape of the paddle
ball.color("white")  # give a color for the paddle
ball.penup()
ball.goto(0, 0)
# separate the ball movement into two parts, the x and y movement
ball.dx = 0.3  # change in x, move by 0.3 pixel
ball.dy = 0.3  # change in y. move by 0.3 pixel

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))


# Create a function
def paddle_a_up():
    y = paddle_a.ycor()  # get the original y coordinate of the paddle
    if y < 290:
        y += 20
    else:
        y = 290
    paddle_a.sety(y)  # set the paddle y coordinate to the new y coordinate


def paddle_a_down():
    y = paddle_a.ycor()  # get the original y coordinate of the paddle
    if y > -290:
        y -= 20
    else:
        y = -290
    paddle_a.sety(y)  # set the paddle y coordinate to the new y coordinate


def paddle_b_up():
    y = paddle_b.ycor()  # get the original y coordinate of the paddle
    if y < 290:
        y += 20
    else:
        y = 290
    paddle_b.sety(y)  # set the paddle y coordinate to the new y coordinate


def paddle_b_down():
    y = paddle_b.ycor()  # get the original y coordinate of the paddle
    if y > -290:
        y -= 20
    else:
        y = -290
    paddle_b.sety(y)  # set the paddle y coordinate to the new y coordinate


# Keyboard binding
win.listen()  # listen for keyboard inputs
win.onkeypress(paddle_a_up, "w")  # when the user press 'w', call the function paddle_a_up
win.onkeypress(paddle_a_down, "s")  # when the user press 's', call the function paddle_a_down
win.onkeypress(paddle_b_up, "Up")  # when the user press the up bottom, call the function paddle_b_up
win.onkeypress(paddle_b_down, "Down")  # when the user press the down bottom, call the function paddle_b_down

# Main game loop
while True:
    win.update()  # every time the loop runs, it update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # set the x coordinate to the new x coordinate
    ball.sety(ball.ycor() + ball.dy)  # set the y coordinate to the new y coordinate

    # Border checking
    if ball.ycor() > 290:  # since the border is 300 and the ball has a dimension of 20
        ball.sety(290)  # set the y coordinate to 290
        ball.dy *= -1  # reverses the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # play the bounce sound

    if ball.ycor() < -290:  # if the ball is going off the bottom border
        ball.sety(-290)  # set the y coordinate to -290
        ball.dy *= -1  # reverses the direction of the ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # play the bounce sound

    if ball.xcor() > 390:  # if the ball is going off the right side
        ball.goto(0, 0)  # reset the ball to the centre of the window
        ball.dx *= -1  # reverse the direction of the ball
        score_a += 1
        pen.clear()  # clear the screen before reprint
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # if the ball is going off the left side
        ball.goto(0, 0)  # reset the ball to the centre of the window
        ball.dx *= -1  # reverse the direction of the ball
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # if the ball is going off the page and is not touching the paddle
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # play the bounce sound

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # play the bounce sound
