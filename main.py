import sys
from RockPaperScissors import RockPaperScissors

RPS = RockPaperScissors()

def startNewGame():
    option = input('Start new game Y/N: ')
    if option.lower() == 'y':
        return True
    else: 
        return False

def main():
    run = True
    while run:
        RPS.simulate()
        
        if not startNewGame():
            run = False
            sys.exit()


if __name__ == "__main__":
    main()