from Die import Die
from time import sleep

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice = []
        self.dice.append(Die())
        self.keeps = [" "," "," "," "," "," "]

    def takeTurn(self):
        turnScore
        turnGoing = True
        while turnGoing:

            for i in range(len(self.dice)):
                if self.keeps[i] != " ":
                    self.dice[i].roll()

            print(f'''You rolled:
    1       2      3      4      5      6
  _____   _____   _____   _____   _____   _____
|       |       |       |       |       |       |
|  {self.dice[0].value}  |  {self.dice[1].value}  |  {self.dice[2].value}  |  {self.dice[3].value}  |  {self.dice[4].value}  |  {self.dice[5].value}  |
|       |       |       |       |       |       |
  _____   _____   _____   _____   _____   _____
|  {self.keeps[0]}  |  {self.keeps[1]}  |  {self.keeps[2]}  |  {self.keeps[3]}  |  {self.keeps[4]}  |  {self.keeps[5]}  |''')
            
            print("Enter a number of a dice you want to keep")
            print("Enter reroll once you are finished")
            print("Enter done to keep and add to your score")
            if self.score == 0:
                print("You must score 450 points in one turn to start scoring!")
            choice = input()
            
            if choice.isnumeric():
                self.keeps[int(choice) - 1] = True
            elif choice == "reroll":
                continue
            elif choice == "done":
                self.score += self.getScore()
            else:
                print("response not reocgnized")
                sleep(3)


    def getScore(self):


            

        

    