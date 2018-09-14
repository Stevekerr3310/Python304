import random

def print_board(board):
    print("-----")
    print("{}|{}|{}".format(board[0], board[1], board[2]))
    print("-----")
    print("{}|{}|{}".format(board[3], board[4], board[5]))
    print("-----")
    print("{}|{}|{}".format(board[6], board[7], board[8]))
    print("-----")
    
def is_win_or_lose(board, choice):
    if ( (board[0] == choice and board[1] == choice and board[2] == choice) or
         (board[3] == choice and board[4] == choice and board[5] == choice) or
         (board[6] == choice and board[7] == choice and board[8] == choice) or
         (board[0] == choice and board[3] == choice and board[6] == choice) or
         (board[1] == choice and board[4] == choice and board[7] == choice) or
         (board[2] == choice and board[5] == choice and board[8] == choice) or
         (board[0] == choice and board[4] == choice and board[8] == choice) or
         (board[2] == choice and board[4] == choice and board[6] == choice)
       ):
        return True
    else:
        return False

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

print("歡迎光臨井字遊戲!!!")
print("請選擇 'O' 或 'X'")

player_choice = input()
if player_choice == "O":
    computer_choice = "X"
else:
    computer_choice = "O"
print("你選擇了",player_choice)
print_board(board)

while True:
    print("請選擇你的下一步：")
    step = int(input())
    board[step -1] = player_choice
    print_board(board)
    
    count = 0
    for i in range(0, len(board)):
        if board[i] != " ":
            count += 1
    if count == 9:
        print("平手")
        print("結束此遊戲")
        break
    
    #判斷輸贏
    if is_win_or_lose(board, player_choice):
        print("恭喜你贏了!")
        print("感謝你玩此遊戲!")
        break

    print("電腦出步了")
    computer_step = random.randint(1,9)
    while board[computer_step - 1] != " ":
        computer_step = random.randint(1,9)
    board[computer_step - 1] = computer_choice
    print_board(board)
    
    #判斷輸贏
    if is_win_or_lose(board, computer_choice):
        print("電腦贏了!")
        break