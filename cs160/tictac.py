

def drawboard(board):
        print(" " + str(board[2][0]) + "  | " + str(board[2][1]) + "  | " + str(board[2][2]))
        print("---------------")
        print(" " + str(board[1][0]) + "  | " + str(board[1][1]) + "  | " + str(board[1][2]))
        print("---------------")
        print(" " + str(board[0][0]) + "  | " + str(board[0][1]) + "  | " + str(board[0][2]))

def print_player1(board, player1, player2):
        spot = raw_input("Player 1: Where would you like to put your " + player1 + ": ")
        #write code to check if spot is already filled
        #write code to check if the spot is within the board
        list(spot) #makes the string input into a list so we can access both numbers the user entered and ignore the space 
        x=int(spot[0])
        y=int(spot[2])
        board[x][y] = player1
        drawboard(board)

def print_player2(board, player1, player2):
        spot = raw_input("Player 2: Where would you like to put your " + player2 + ": ")
        #write code check if the spot is already filled
        #write code to check if the spot is within the board
        list(spot)
        x=int(spot[0])
        y=int(spot[2])
        board[x][y]= player2
        drawboard(board)
def check_win(board, player1, player2):
        #write code to check if there is a win
        countx=0
        county=0
        
        for i in range(3):
                for j in range(3):
                        if str(board[i][j]) == player1:
                                countx+=1
                        elif str(board[i][j]) == player2:
                                county+=1

        if countx >=3:
                #check diagnal
                if board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
                        return True
                elif board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
                        return True
                #check across
                elif board[0][0] == player1 and board[0][1] == player1 and board[0][2] == player1:
                        return True
                elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
                        return True
                elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
                        return True
                #check down
                elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
                        return True
                elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
                        return True
                elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
                        return True
        if county >=3:
                #check diagnal
                if board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2:
                        return True
                elif board[0][2] == player2 and board[1][1] == player2 and board[2][0] == player2:
                        return True
                #check across
                elif board[0][0] == player2 and board[0][1] == player2 and board[0][2] == player2:
                        return True
                elif board[1][0] == player2 and board[1][1] == player2 and board[1][2] == player2:
                        return True
                elif board[2][0] == player2 and board[2][1] == player2 and board[2][2] == player2:
                        return True
                #check down
                elif board[0][0] == player2 and board[1][0] == player2 and board[2][0] == player2:
                        return True
                elif board[1][0] == player2 and board[1][1] == player2 and board[1][2] == player2:
                        return True
                elif board[2][0] == player2 and board[2][1] == player2 and board[2][2] == player2:
                        return True
                
        #use a loop to iterate through the array and check if there are matching characters across, down, or diagnol for both players
def main():
        done = False
        rows, cols = (3, 3) 
        board = [[" " for i in range(cols)] for j in range(rows)] 
        drawboard(board)
        numplayers= input("Do you want 1 or 2 players? ")
        if numplayers == 1:
                player1 = raw_input("Player 1: What character do you want? ")
                #write code to play the game with just one player
                #add a random spot generator for the computer to put a character
        if numplayers == 2:
                player1 = raw_input("Player 1: What character do you want? ")
                player2 = raw_input("Player 2: What character do you want? ")
                while player1 == player2:
                        player2 = raw_input("Player 2, please pick a different character: ")
        while done == False:
             print_player1(board, player1, player2)
             win = check_win(board, player1, player2)
             if win == True:
                     done = True
                     print("Player 1 Wins!")
                     break
             print_player2(board, player1, player2)
             win = check_win(board, player1, player2)
             if win == True:
                     done = True   
                     print("Player 2 Wins!")
                     break   

main()
