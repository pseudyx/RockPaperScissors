import random, sys

Options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
Outcomes = {
    "Rock": lambda computerChoice : printOutcome('Rock', computerChoice, ['Scissors', 'Lizard'], ['Paper', 'Spock']),
    "Paper": lambda computerChoice : printOutcome('Paper', computerChoice, ['Rock', 'Spock'], ['Scissors', 'Lizard']),
    "Scissors": lambda computerChoice : printOutcome('Scissors', computerChoice, ['Paper', 'Lizard'], ['Spock', 'Rock']),
    "Lizard": lambda computerChoice : printOutcome('Lizard', computerChoice, ['Spock', 'Paper'], ['Scissors', 'Rock']),
    "Spock": lambda computerChoice : printOutcome('Spock', computerChoice, ['Scissors', 'Rock'], ['Lizard', 'Paper'])
}

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

    Outcomes[playerChoice](computerChoice)

def startNewGame():
    option = input('Start new game Y/N: ')
    if option.lower() == 'y':
        return True
    else: 
        return False

def main():
    run = True
    while run:
        printOptions()
        playerChoice = getPlayerChoice()
        computerChoice = getComputerChoice()

        printChoices(playerChoice,computerChoice)
        printResult(playerChoice, computerChoice)
        
        if not startNewGame():
            run = False
            sys.exit()

main()
