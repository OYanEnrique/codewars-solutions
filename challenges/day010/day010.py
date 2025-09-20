'''Let's play! You have to return which player won! In case of a draw return Draw!'''

def rps(p1, p2):
    play = (p1,p2)
    if p1 == p2:
        return "Draw!"
    if play in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
        return "Player 1 won!"
    else:
        return "Player 2 won!"	
