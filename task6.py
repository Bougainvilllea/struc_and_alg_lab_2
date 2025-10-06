import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)
        t.right(120)
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)

def draw_koch_snowflake(length=300, depth=3):
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Снежинка Коха")

    t = turtle.Turtle()
    t.speed(0)  
    t.hideturtle()

    t.penup()
    t.goto(-length / 2, -length / (2 * (3 ** 0.5)))
    t.pendown()

    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

    screen.exitonclick()

if __name__ == "__main__":
    draw_koch_snowflake(length=300, depth=4)