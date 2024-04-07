import sys
import os 
import random


# This is my TicTacToe Class 
class TicTacToe:
    # Declare class variables 
    # players is a list of players (this game will have 2 players)
    # Winninggames is a list of all winning possibilities 
    # Player1entry is a list of entries of first players 
    # Player2 entry is a list of entries of second player 
    players = []
    winninggames = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    player1entry = []
    player2entry = []
    board = [1,2,3,4,5,6,7,8,9] #Based on infromation given in the Final Exam Problem Statement


    # This is a constructor method
    """
    This is a constructor that prints an initialization statement
    Then call the getplayernames method to get the names and configure the list of players 
    Also call the printboard method to print the board, since this is a constructor the printboard is called first time here 
    Therefore printboard in this constructor will print initial brand new board ready to be played.
    """
    def __init__(self) -> None:
        print ("Initializing a 3X3 TicTacToe")
        self.getplayernames()
        self.printboard()    
    """
    This is getplayernames method 
    This method asks user to enter the name of the player 1 and 2 one by one and append the names to the players class variable
    """
    def getplayernames(self): 
        player1 = input("What is the name of the player 1: ")
        player2 = input("What is the name of the player 2: ")
        self.players.append(player1)
        self.players.append(player2)
        
    """
    This is a printboard method 
    This method prints current state of the board 
    """
    def printboard(self):
        print(f"|{self.board[0]}|{self.board[1]}|{self.board[2]}|")
        print(f"|{self.board[3]}|{self.board[4]}|{self.board[5]}|")
        print(f"|{self.board[6]}|{self.board[7]}|{self.board[8]}|")
    
    """
    This method gets all available numbers to be played at the time this method is called 
    It returns these available numbers 
    :return availablenumbers 
    """
    def getavailablenumbers(self):
        availablenumbers = []
        for i in range(len(self.board)):
            if self.board[i] != 'X' and self.board[i] != 'O':
                availablenumbers.append(self.board[i])
        return availablenumbers
    
    
    """
    This function goes through all the winning games and compare them against the each individual players entries
    By comparing the entries against winning game this method identifies the winner if there is one 
    If there is a winner this method returns the winner otherwise return None
    """
    def getwinner(self):
        for win in self.winninggames:
            if all(self.board[num] == 'X' for num in win):
                return self.players[0]
            elif all(self.board[num] == 'O' for num in win):
                return self.players[1]
        if len(self.getavailablenumbers()) == 0:
            return None
        
        
    """
    This is rungame method 
    This method continue to run a loop asking the user to enter the number to play and shows the available numbers as well
    If the user enter something otherthan the available number the prompt will continue to ask the same user to enter the correct values 
    This method assembles all the relevant method we have together, so that 
    First player one is asked to enter the number and then the second and then the first and it keep alternates 
    Until one player wins or the game finishes where there is no further numbers to enter. 
    Ultimately, if there is a winner it prints the winner. If ther eis no winner it prints No Winner. 
    """
    def rungame(self): 
        player_turn = 0
        while True:
            available_variables = self.getavailablenumbers()
            latestplayers = self.players[player_turn % 2]
            
            if player_turn < 9:
                if player_turn%2 == 0:
                    selected_number = input(f"{latestplayers} Enter the number to play your symbol X (Available Numbers {','.join(map(str, available_variables))}): ")
                else:
                    selected_number = input(f"{latestplayers} Enter the number to play your symbol O (Available Numbers {','.join(map(str, available_variables))}): ")
                if selected_number.strip() == "":
                    continue 

                if selected_number.isdigit():
                    selected_number = int(selected_number)

                    if selected_number in available_variables:
                        if player_turn % 2 == 0:
                            self.player1entry.append(selected_number)
                            self.board[selected_number - 1] = 'X'
                        else:
                            self.player2entry.append(selected_number)
                            self.board[selected_number - 1] = 'O'
                        winner = self.getwinner()
                        if winner:
                            print(f"Player {winner} is the winner")
                            break
                        self.printboard()
                        if winner == None and player_turn == 8:
                            print("No one win!")
                            print("End of the game",end='')  
                            break
                        player_turn += 1
                        
                    else:
                        print(f"Number already played, choose a different number from available numbers. (Available Numbers %s) {','.join(map(str, available_variables))}")
                else:
                    print("Enter available Number")

# My main method to test this code locally
if __name__ == "__main__":
    game = TicTacToe()
    game.rungame()
      