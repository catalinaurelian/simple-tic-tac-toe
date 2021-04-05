##The order of the grid is just like your numpad.

board = {   '7':'  ', '8':'  ', '9':'  ' ,
            '4':'  ', '5':'  ', '6':'  ' ,
            '1':'  ', '2':'  ', '3':'  ' }

turn = True

def updateBoard():
    print(board['7'] + "|" + board['8'] + "|" + board['9'] + "\n" + board['4'] + "|" + board['5'] + "|" + board['6']+  "\n" + board['1'] + "|" + board ['2'] + "|"  + board['3'])

def choice():
    n = int(input("What position will you choose?"))
    if(n>=1 and n<=9):
        if(turn == 0):
            board[str(n)] = "X"
        elif(turn == 1):
            board[str(n)] = "0"
    else:
        print("Incorrect value! Please pick an existing square!")



def checkForWinX():
    if(board['7']==board['8']==board['9']=="X" or
    board['4']==board['5']==board['6']=="X" or
    board['1']==board['2']==board['3']=="X" or
    board['7']==board['4']==board['1']=="X" or
    board['8']==board['5']==board['2']=="X" or
    board['9']==board['6']==board['3']=="X" or
    board['7']==board['5']==board['3']=="X" or
    board['1']==board['5']==board['9']=="X"):
        print("Game over.")
        print("X has won the game.")
        exit()

def checkForWin0():
    if(board['7']==board['8']==board['9']=="0" or
    board['4']==board['5']==board['6']=="0" or
    board['1']==board['2']==board['3']=="0" or
    board['7']==board['4']==board['1']=="0" or
    board['8']==board['5']==board['2']=="0" or
    board['9']==board['6']==board['3']=="0" or
    board['7']==board['5']==board['3']=="0" or
    board['1']==board['5']==board['9']=="0"):
        print("Game over.")
        print("0 has won the game.")
        exit()


def game():
    count = 0
    while(1):

        global turn
        turn = not turn

        updateBoard()
        choice()
        if count>=4:
            checkForWinX()
            checkForWin0()
        count = count + 1
        if count == 9:
            print("Tie!")
            updateBoard()
            exit()

game()
