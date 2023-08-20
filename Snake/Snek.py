import turtle
import random
import time
import winsound
from save_load import save_list, load_list

database = {}
database = dict(load_list("highScore.json"))
highScore = 0
while True:
    print()
    options = input("1.Leaderboard\n2.Play\n")
    if options == "1":
        print("Players:\n",*database.keys())
        name = input("Choose a player name to view their high score: ")
        if name not in database.keys():
              print("Username not found")
              continue
        else:
            print(f"\n{name}'s high score is : ",database[name])
            continue
    if options == "2":
        name = input("Player's name: ")
        if name in database.keys():
              highScore = database[name]
              break
        else:
            database[name] = (highScore)
            save_list(database, "highScore.json")
            break
       


score = 0

delay=0.1
window = turtle.Screen()
window.title("Snake🐍")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)


head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction="stop"

food = turtle.Turtle()
colors = random.choice(["red","green"])
food.color(colors)
food.shape("circle")
food.shapesize(-1,-1,0)
food.penup()
food.speed(0)
food.goto(0,100)

pen = turtle.Turtle()
highScorePen = turtle.Turtle()

pen.color("white")
highScorePen.color("white")
pen.shape("square")
pen.penup()
highScorePen.penup()
pen.speed(0)
pen.hideturtle()
highScorePen.hideturtle()
pen.goto(-100,250)
pen.clear()
pen.write(f"{name}'s score: {score}",font=("candara", 13, "normal"))
highScorePen.goto(70,250)
highScorePen.write(f"{name}'s high_score: {highScore}",font=("candara", 13, "normal"))



# Snake movment
def right():
            winsound.PlaySound("Right.wav", True)
            head.direction="right"
    
def left():
            winsound.PlaySound("Left.wav", True)
            head.direction="left"

def up():
            winsound.PlaySound("Up.wav", True)
            head.direction="up"
            
    
def down():
            winsound.PlaySound("Down.wav", True)
            head.direction="down"
def move():
    if head.direction == "up":
            y = head.ycor()
            head.sety(y+20)
            
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

window.listen()
window.onkey(right,"Right")
window.onkey(left,"Left")
window.onkey(up,"Up")
window.onkey(down,"Down")
body=[] 
score=0
delay=.1
def collision():
    winsound.PlaySound("Lost.wav", True)
    time.sleep(1)
    head.goto(0,0)
    head.direction="stop"
   

# Game Loop
while True:
    window.update()
    if head.xcor() > 279.9897 or head.xcor() < -279.9897 or head.ycor() > 279.9897 or head.ycor() < -279.9897:
        winsound.PlaySound("Lost.wav", True)
        collision()
        for part in body:
            part.goto(1000,1000)
        body.clear()
        score = 0
        delay = 0.1
        pen.clear()
        #pen.write("score",align="center",font=("candara", 13, "normal"))
    if head.distance(food) <=19:
        winsound.PlaySound("crunch.wav", True)
        food.goto(x=random.randint(-280,280),y=random.randint(-280,280))
        #increase the lenghth of snake
        new_part=turtle.Turtle()
        new_part.shape("square")
        new_part.color("Purple") 
        new_part.speed(0)   
        new_part.penup()

        body.append(new_part)
        # delay -=.001
        score +=1
  
        pen.clear()
        pen.write(f"{name}'s score: {score}",font=("candara", 13, "normal"))
        if score > highScore:
              highScore = score
              highScorePen.clear()
              highScorePen.write(f"{name}'s high_score: {highScore}",font=("candara", 13, "normal"))
              database[str(name)]= highScore
              save_list(database, "highScore.json")


        #The connection of the head with the parts of the body
    for index in range(len(body)-1, 0, -1):
            x = body[index-1].xcor()
            y = body[index-1].ycor()
            body[index].goto(x, y)
    if len(body) > 0:
            x = head.xcor()
            y = head.ycor()

            body[0].goto(x, y)
    move()
    for part in body:
            if part.distance(head) < 20:
                collision()
                for part in body:
                    part.goto(1000, 1000)
                body.clear()
                score = 0
                delay = 0.1
                pen.clear()
    time.sleep(delay)
        
window.mainloop()
       
    
            

        