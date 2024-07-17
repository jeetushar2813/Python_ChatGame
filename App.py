import turtle

# Function to start the Pong game
def pong_game():
    # Set up the screen
    win = turtle.Screen()
    win.title("Pong Game")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=6, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=6, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(40)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 3  # Increase this value to make the ball move faster along the x-axis
    ball.dy = -3  # Increase this value to make the ball move faster along the y-axis

    # Function to move paddle A up
    def paddle_a_up():
        y = paddle_a.ycor()
        if y < 250:
            y += 20
            paddle_a.sety(y)

    # Function to move paddle A down
    def paddle_a_down():
        y = paddle_a.ycor()
        if y > -240:
            y -= 20
            paddle_a.sety(y)

    # Function to move paddle B up
    def paddle_b_up():
        y = paddle_b.ycor()
        if y < 250:
            y += 20
            paddle_b.sety(y)

    # Function to move paddle B down
    def paddle_b_down():
        y = paddle_b.ycor()
        if y > -240:
            y -= 20
            paddle_b.sety(y)

    # Keyboard bindings
    win.listen()
    win.onkeypress(paddle_a_up, "w")
    win.onkeypress(paddle_a_down, "s")
    win.onkeypress(paddle_b_up, "Up")
    win.onkeypress(paddle_b_down, "Down")

    # Main game loop
    try:
        while True:
            win.update()

            # Move the ball
            ball.setx(ball.dx + ball.xcor())
            ball.sety(ball.dy + ball.ycor())

            # Border checking
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.dx *= -1

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dx *= -1

            # Paddle and ball collision
            if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
                ball.setx(340)
                ball.dx *= -1

            if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
                ball.setx(-340)
                ball.dx *= -1
    except turtle.Terminator:
        print("Game closed.")

# User access check
Player_1 = input("What's Player A's Name: ")
Player_2 = input("What's Player B's Name: ")
print(f"{Player_1} vs {Player_2}! Get ready, let's go!")
pong_game()

