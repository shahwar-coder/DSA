'''
3. Rock–Paper–Scissors Outcome
Task:
Implement a function rps_winner(p1: str, p2: str) -> str that takes two players’ choices—each one of "rock", "paper", or "scissors"—and returns:

"Player 1 wins"
"Player 2 wins"
"Tie"

Use nested if statements (or a clear chain of if/elif/else) to compare p1 and p2. Validate inputs: if either choice is not one of the three, raise a ValueError.
'''

def rps_winner(p1: str, p2: str)->str:
    """Return the winner of the game Rock-Paper-Scissors"""
    
    if p1=="rock":
        if p2=="rock":
            return "Tie"
        elif p2=="paper":
            return "Player 2 wins"
        elif p2=="scissors":
            return "Player 1 wins"
        else:
            raise ValueError("Player 2 should choose from either rock, paper or scissors")
    
    elif p1=="paper":
        if p2=="rock":
            return "Player 1 wins"
        elif p2=="paper":
            return "Tie"
        elif p2=="scissors":
            return "Player 2 wins"
        else:
            raise ValueError("Player 2 should choose from either rock, paper or scissors")
    
    elif p1=="scissors":
        if p2=="rock":
            return "Player 2 wins"
        elif p2=="paper":
            return "Player 1 wins"
        elif p2=="scissors":
            return "Tie"
        else:
            raise ValueError("Player 2 should choose from either rock, paper or scissors")
    else:
            raise ValueError("Player 1 should choose from either rock, paper or scissors")

def main():
    p1=input("P1 : ")
    p2=input("P2 : ")
    print(rps_winner(p1, p2))

if __name__=="__main__":
    main()
