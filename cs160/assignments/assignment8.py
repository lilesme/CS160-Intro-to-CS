import sys

def init_board(r,c):
    board = [' ']*r
    for i in range(r):
        board[i] = [' ']*c

    r=int(r)
    x=int(r/2)
    board[x-1][x-1]='X'
    board[x][x]='X'
    board[x][x-1]='O'
    board[x-1][x]='O'

    r=str(r)

    return board

def print_board(board, c):
    #print first row of dashes

    for y in range(c):
        print("  " + str(y)+ " ", end="")
    print("")
    for n in range(c):
        print("  __", end="")
    print("")
    #for the number of rows
    for i in range(len(board)):
        #for the number of columns
        print(str(i), end="")
        for j in range(len(board[i])):
            #print the tokens
            print("|  " + board[i][j], end="")
        print("|")
        #print row of dashes between rows
        for l in range(c):
            print("  __", end="")
        print("")
    print("")

def change_token(x, y, player, board):
    board[y][x]=player

def place_token(x, y, player, board):
    board[y][x]=player


def check_lower_left(x, y, player, board, r, c):
    if y-2 < 0 or x-2 < 0:
        return False
    n=y+2 #(y values)
    p=x-2 #(x values)
    while n < r and p > 0:
        if board[n][p]==player:
            place_token(p, n, player, board)
            #while current spot is less than placed token
            while n > y and p < x:
                n=n-1
                p=p+1
                change_token(p, n, player, board)
            return True
        #iterate down and left
        n=n+1
        p=p-1
    return False

def check_lower_right(x, y, player, board, r, c):
    if y-2 < 0 or x+2 > c-1:
        return False
    n=y+2 #(y values)
    p=x+2 #(x values)
    while p < c and n < r:
        if board[n][p]==player:
            place_token(p, n, player, board)
            #while current spot is less than placed token
            while p > x and n > y:
                n=n-1
                p=p-1
                change_token(p, n, player, board)
            return True
        #iterate down and right
        n=n+1
        p=p+1
    return False

def check_upper_left(x, y, player, board, r, c):
    if y-2 < 0 or x-2 < 0:
        return False
    n=y-2 #(y values)
    p=x-2 #(x values)
    while n > 0 and p > 0:
        if board[n][p]==player:
            place_token(p, n, player, board)
            #while current spot is less than placed token
            while p < x and n < y:
                p=p+1
                n=n+1
                change_token(p, n, player, board)
            return True
        #iterate up and left
        n=n-1
        p=p-1
    return False

def check_upper_right(x, y, player, board, r, c):
    if y+2 > r-1 or x+2 > c-1:
        return False
    n=y-2 #(y values)
    p=x+2 #(x values)
    while n > 0 and p < c:
        if board[n][p]==player:
            place_token(p, n, player, board)
            #while current spot is less than placed token
            while n < y and p > x:
                n=n+1
                p=p-1
                change_token(p, n, player, board)
            return True
        #iterate up and right
        n=n-1
        p=p+1
    return False

def check_down(x, y, player, board, r, c):
    if y+2 > r-1:
        return False
    n=y+2
    while n < r:
        if board[n][x]==player:
            place_token(x, n, player, board)
            #while current spot is less than placed token
            while n > y:
                n=n-1
                change_token(x, n, player, board)
            return True
        #iterate down
        n=n+1
    return False

def check_up(x, y, player, board, r, c):
    if y-2 < 0:
        return False
    n=y-2
    while n > 0:
        if board[n][x]==player:
            place_token(x, y, player, board)
            #while current spot is less than placed token
            while n < y:
                n=n+1
                change_token(x, n, player, board)
            return True
        #iterate up
        n=n-1
    return False

def check_right(x, y, player, board, r, c):
    if x+2 > c-1:
        return False
    n=x+2
    while n < c:
        if board[y][n]==player:
            place_token(x, y, player, board)
            #while current spot is less than placed token
            while n > x:
                n=n-1
                change_token(n, y, player, board)
            return True
        #iterate right
        n=n+1
    return False

def check_left(x, y, player, board, r, c):
    if x-2 < 0:
        return False
    n=x-2
    while n > 0:
            if board[y][n]==player:
                place_token(x, y, player, board)
                #while current spot is less than placed token
                while n < x:
                    n=n+1
                    change_token(n, y, player, board)
                return True
            n=n-1
    return False

def check_move(x, y, player, board, r, c):
    if x > c-1 or x < 0:
        print("That is not a valid move!")
        get_move(player, board, r, c)
    elif y > r or y < 0:
        print("That is not a valid move!")
        get_move(player, board, r, c)

    valid1=check_left(x, y, player, board, r, c)
    valid2=check_right(x, y, player, board, r, c)
    valid3=check_up(x, y, player, board, r, c)
    valid4=check_down(x, y, player, board, r, c)
    valid5=check_upper_right(x, y, player, board, r, c)
    valid6=check_upper_left(x, y, player, board, r, c)
    valid7=check_lower_right(x, y, player, board, r, c)
    valid8=check_lower_left(x, y, player, board, r, c)

    if valid1==False and valid2==False:
        if valid3==False and valid4==False:
            if valid5==False and valid6==False:
                if valid7==False and valid8==False:
                    print("That is not a valid move!")
                    get_move(player, board, r, c)

def get_move(player, board, r, c):
        retry=True
        while retry==True:
            y=int(input("Please enter the row number (Side Numbers): "))
            x=int(input("Please enter the column number (Top Numbers): "))
            #check if there is a token there
            if x > c-1 or x < 0:
                print("That is not a valid move!")
                retry=True
            elif y > r or y < 0:
                print("That is not a valid move!")
                retry=True
            else:
                retry=False

        correct=False
        while correct==False:
            if board[y][x] != " ":
                print("There is already a token there!")
                correct=False
                y=int(input("Please enter the row number (Side Numbers): "))
                x=int(input("Please enter the column number (Top Numbers): "))
            else:
                correct=True
                check_move(x, y, player, board, r, c)




def change_player(player):
    if player=='X':
        player='O'
    elif player=='O':
        player='X'

    return player

def turn(player):
    if player=='X':
        print("Black's Turn!")
    elif player=='O':
        print("White's Turn!")


def check_win(r, c, board):
    num_blacks=0
    num_whites=0
    #check if no more valid moves

    #count number of whites and blacks:
    for i in range(r):
        for j in range(c):
            if board[i][j]==' ':
                return False
            if board[i][j]=='O':
                num_whites=num_whites + 1
            elif board[i][j]=='X':
                num_blacks= num_blacks + 1
    print("Number of Black Tokens: ", num_blacks)
    print("Number of White Tokens: ", num_whites)
    if num_whites > num_blacks:
        print("White Wins!")
    elif num_blacks > num_whites:
        print("Black Wins!")
    else:
        print("It's a Tie!")

    return True


def main():
    #set up the board
    again=True
    win=False
    ready=False
    player='X'
    while (len(sys.argv)!=3):
        print("Not the correct number of arguments!")
        return
    r=int(sys.argv[1]) #rows arg 1
    c=int(sys.argv[2]) #columns arg 2

    while again==True:
        while ready==False:
            if r != c:
                print("That is not a square board!")
                ready=False
                r=int(input("Please enter the rows: "))
                c=int(input("Please enter the cols: "))

            elif r%2 != 0:
                print("The board must have even integer dimensions!")
                ready=False
                r=int(input("Please enter the rows: "))
                c=int(input("Please enter the cols: "))

            elif r < 8:
                print("The board must be 8X8 or larger!")
                ready=False
                r=int(input("Please enter the rows: "))
                c=int(input("Please enter the cols: "))

            else:
                ready=True

        board=init_board(r, c)
        print_board(board, c)

        while win==False:
            turn(player)
            move=get_move(player, board, r, c)
            print_board(board, c)
            win=check_win(r, c, board)
            player=change_player(player)

        x=int(input("Would you like to play again? 1-Yes or 2-No: "))
        if x==1:
            again=True
            r=int(input("Please enter the rows: "))
            c=int(input("Please enter the cols: "))
        else:
            again=False





main()
