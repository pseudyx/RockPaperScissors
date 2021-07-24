import random

class RockPaperScissors:
    def __init__(self):
        self.Options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.Outcomes = {
            "Rock": lambda : self.printOutcome(['Scissors', 'Lizard'], ['Paper', 'Spock']),
            "Paper": lambda : self.printOutcome(['Rock', 'Spock'], ['Scissors', 'Lizard']),
            "Scissors": lambda : self.printOutcome(['Paper', 'Lizard'], ['Spock', 'Rock']),
            "Lizard": lambda : self.printOutcome(['Spock', 'Paper'], ['Scissors', 'Rock']),
            "Spock": lambda : self.printOutcome(['Scissors', 'Rock'], ['Lizard', 'Paper'])
        }
        self.computerChoice = None
        self.playerChoice = None

    def getComputerChoice(self):
        self.computerChoice = random.choice(self.Options)

    def getPlayerChoice(self):
        self.playerChoice = self.Options[int(input('Enter the number of your choice: '))-1]

    def printOptions(self):
        print('\n'.join(f'({i+1}) {option.title()}' for i, option in enumerate(self.Options)))

    def printChoices(self):
        print(f'You chose {self.playerChoice}')
        print(f'The computer chose {self.computerChoice}')

    def printOutcome(self, choiceBeats, choiceLoseTo):
        if self.computerChoice in choiceLoseTo:
            print(f'Sorry {self.computerChoice} beats {self.playerChoice}' )
        elif self.computerChoice in choiceBeats:
            print(f'Yes! {self.playerChoice} beats {self.computerChoice}')
        print('\n')

    def printResult(self):
        if self.playerChoice == self.computerChoice:
            print("Draw!")

        self.Outcomes[self.playerChoice]()

    def simulate(self):
        self.printOptions()
        self.getPlayerChoice()
        self.getComputerChoice()
        self.printChoices()
        self.printResult()
