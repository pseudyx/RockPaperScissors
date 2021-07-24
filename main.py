import random, sys

Options = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]

def getComputerChoice():
    return random.choice(Options)

def getPlayerChoice():
    return Options[int(input('Enter the number of your choice: '))-1]

def printOptions():
    print('\n'.join(f'({i+1}) {option.title()}' for i, option in enumerate(Options)))

def printChoices(playerChoice, computerChoice):
    print(f'You chose {playerChoice}')
    print(f'The computer chose {computerChoice}')

def printOutcome(playerChoice, computerChoice, choiceBeats, choiceLoseTo):
    if computerChoice in choiceLoseTo:
        print(f'Sorry {computerChoice} beats {playerChoice}' )
    elif computerChoice in choiceBeats:
        print(f'Yes! {playerChoice} beats {computerChoice}')
    print('\n')

def printResult(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        print("Draw!")

    if playerChoice == 'Rock':
        printOutcome('Rock', computerChoice, ['Scissors', 'Lizzard'], ['Paper', 'Spock'])
    elif playerChoice == "Paper":
        printOutcome('Paper', computerChoice, ['Rock', 'Spock'], ['Scissors', 'Lizzard'])
    elif playerChoice == "Scissors":
        printOutcome('Scissors', computerChoice, ['Paper', 'Lizzard'], ['Spock', 'Rock'])
    elif playerChoice == "Lizzard":
        printOutcome('Lizzard', computerChoice, ['Spock', 'Paper'], ['Scissors', 'Rock'])
    elif playerChoice == "Spock":
        printOutcome('Spock', computerChoice, ['Scissors', 'Rock'], ['Lizzard', 'Paper'])

def startNewGame():
    option = input('Start new game Y/n: ')
    if option == 'n':
        return 'n'
    else: 
        return 'y'

def main():
    run = True
    while run:
        printOptions()
        playerChoice = getPlayerChoice()
        computerChoice = getComputerChoice()

        printChoices(playerChoice,computerChoice)
        printResult(playerChoice, computerChoice)
        playerChoice = startNewGame()

        if playerChoice == "n":
            run = False
            sys.exit()

main()