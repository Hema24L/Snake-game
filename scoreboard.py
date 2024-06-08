from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake-game\highscore.txt") as file:
            data = file.read()
            file.close()
        self.highscore = int(data)
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High-Score:{self.highscore}", align='center', font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake-game\highscore.txt", "w") as file:
                file.write(repr(self.highscore))
                file.close()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 16, 'normal'))

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
