import random

#提示訊息
def prompt():
    print("------ ! 歡迎來到剪刀石頭布 ! ------")
    print("請出拳 (1) 剪刀  (2) 石頭  (3) 布:")
    
def promptPlayAgain():
    print("要繼續玩嗎? 1)Y 2)N")
    
def promptError():
    print("輸入錯誤，請重新輸入!!")

#顯示猜拳中文
def displayHandName(choice):
    if choice == 1:
        return "剪刀"
    elif choice == 2:
        return "石頭"
    elif choice == 3:
        return "布"

#判斷輸贏
def isWinOrLose(player_hand, computer_hand):
    print("玩家 : {}  電腦 : {}".format(displayHandName(player_hand), displayHandName(computer_hand)))
    if player_hand == computer_hand:
        print("平手!")
    elif (player_hand == 1 and computer_hand == 3) or (player_hand == 2 and computer_hand == 1) or (player_hand == 3 and computer_hand == 2):
        print("你贏了!")
    else:
        print("你輸了!")

play = "Y"
playList = [1, 2, 3]

while play.upper() == "Y":
    prompt()
    player_hand = int(input())
    
    if player_hand not in playList:
        promptError()
        continue
        
    computer_hand = random.randint(1,3)
    isWinOrLose(player_hand, computer_hand)
    promptPlayAgain()
    play = input()
    
    while play.upper() != "Y" and play.upper() != "N":
        promptError()
        promptPlayAgain()
        play = input()
