from player import Player

from colorama import init, Fore, Back
init(autoreset=True)

class Board:
    def __init__(self):
        self.grid = [["-" for _ in range(3)] for _ in range(3)]
        self.moves_count = 0
        self.winner = None
        
        # calc for winner
        self.rowsum = [0]*3
        self.colsum = [0]*3
        self.diagsum = 0
        self.antidiag = 0
    
    def make_move(self, row, col, current_player: Player):
        if self.grid[row][col] != "-": raise ValueError("❌ Position already marked")
        
        # normally
        self.grid[row][col] = "⭕" if current_player.get_symbol() == "O" else "❌"
        self.moves_count += 1
        
        # update board metrics
        score = 1 if current_player.get_symbol() == "X" else -1
        self.rowsum[row] += score
        self.colsum[col] += score
        self.diagsum += score
        self.antidiag += score
        
        # check if won
        if (
            self.rowsum == 3 or
            self.colsum == 3 or
            self.diagsum == 3 or
            self.antidiag == 3
        ): 
            self.winner = current_player
    
    def is_full(self):
        return self.moves_count == 9

    def get_winner(self):
        return self.winner
    
    def print_board(self):
        for row in range(3):
            print(Fore.WHITE + " | ".join(self.grid[row]))
        print()