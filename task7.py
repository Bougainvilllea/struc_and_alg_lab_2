import turtle

def draw_triangle_mountain(t, x, y, width, height, depth):
    if depth <= 0:
        return

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + width / 2, y + height)  
    t.goto(x + width, y)                
    t.goto(x, y)                     

    new_width = width / 2
    new_height = height / 2
    draw_triangle_mountain(t, x, y, new_width, new_height, depth - 1)
    draw_triangle_mountain(t, x + new_width, y, new_width, new_height, depth - 1)

def main():
    screen = turtle.Screen()
    screen.setup(width=900, height=600)
    screen.bgcolor("skyblue")
    screen.title("Фрактальные горы (треугольная версия)")

    t = turtle.Turtle()
    t.speed(0)          
    t.hideturtle()
    t.color("darkgreen")
    t.pensize(2)

    start_x = -300
    start_y = -200
    base_width = 600
    peak_height = 300
    recursion_depth = 5  

    draw_triangle_mountain(t, start_x, start_y, base_width, peak_height, recursion_depth)

    screen.exitonclick()

if __name__ == "__main__":
    main()