from colorama import init, Fore, Back, Style
init(autoreset=True)

from player import Player

class GameMaster:
    def __init__(self, p1: Player, p2: Player):
        self.player1 = p1
        self.player2 = p2
        self.board = Board()
        self.current_player = self.player1 # p1 starts
    
    def play(self):
        # init the board
        self.board.buildBoard()
        
        while not self.board.is_full() and not self.board.get_winner():
            
            # Notify whose turn
            if self.current_player == self.player1:
                print(Fore.BLUE + f"{self.current_player.get_name()}'s turn")
            else:
                print(Fore.RED + f"{self.current_player.get_name()}'s turn")
            
            # validate input
            row = self.validate("Enter row (0-2):")
            col = self.validate("Enter col (0-2):")

            # try to mark on board
            try:
                self.board.make_move(row, col, self.current_player)

                # display updated board
                self.board.print_board()
                
                # other players turn
                self.switch_player()
                
            except ValueError as E:
                print(Back.RED + str(E))
        
        # Someone Won or Board's full
        if self.board.is_full():
            print(Fore.LIGHTRED_EX + f"It is a draw 🙄")
        else:
            print(Fore.LIGHTYELLOW_EX + f"{self.get_winner().get_name()} WINS 🥳")
                

    def switchPlayer(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def validate(self, message):
        while True:
            try:
                userInput = int(input(message, end=" "))
                if 0 <= userInput <= 2:
                    return userInput
                else:
                    raise ValueError("Invalid input ! Please enter a number between 0 and 2")
            except ValueError as E:
                print(Back.RED + E)