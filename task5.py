import turtle
import random

def tree(branchLen, t, thickness):
    if branchLen > 5:
        t.pensize(thickness)
        
        if branchLen < 15:
            t.color("green")
        else:
            t.color("saddlebrown")
        
        t.forward(branchLen)
        
        angle1 = random.randint(15, 45)
        angle2 = random.randint(15, 45)
        
        reduction1 = random.randint(10, 20)
        reduction2 = random.randint(10, 20)
        
        t.right(angle1)
        tree(branchLen - reduction1, t, max(1, thickness * 0.7))
        t.left(angle1 + angle2)
        
        tree(branchLen - reduction2, t, max(1, thickness * 0.7))
        t.right(angle2)
        
        t.backward(branchLen)
        if branchLen >= 15:
            t.color("saddlebrown")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.bgcolor("lightblue")
    
    t.speed(0)  
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    
    initial_thickness = 10
    tree(80, t, initial_thickness)
    
    myWin.exitonclick()

if __name__ == "__main__":
    main()