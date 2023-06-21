from turtle import Turtle

class Score:
    points=-1
    file=open("savefile.txt")
    content=file.read()
    file.close()
    high_score=int(content)
    scoreboard=Turtle() 
    def __init__(self):

        self.scoreboard.goto(0,280)
        self.scoreboard.color('white')
        self.update()

    def update(self):
        self.points+=1
        print(self.points)
        style = ('Times New Roman', 15, 'bold')
        self.scoreboard.clear()
        self.scoreboard.write("Score : "+str(self.points)+" High score: "+str(self.high_score), font=style, align='center')
        self.scoreboard.hideturtle() 

    def reset(self):
        if(self.points>self.high_score):
            newfile=open("savefile.txt",mode="w")
            newfile.write(str(self.points))
            self.high_score=self.points
            newfile.close()

        self.points=-1
        self.update()
          

    def game_over(self):
        game_over=Turtle()
        game_over.color('light blue')
        print(self.points)
        style = ('Times New Roman', 30, 'bold')
        game_over.clear()
        game_over.write("Game Over", font=style, align='center')
        game_over.hideturtle()         
