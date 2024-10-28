from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f'Level: {self.level}', align='left', font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font =FONT)
    
    def level_up(self):
        self.level = self.level + 1