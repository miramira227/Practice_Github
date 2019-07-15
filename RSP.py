import random

while True:

    computer = random.randint(1,3)
    if (computer == 1):
        computer = "가위"
    elif (computer == 2):
        computer = "바위"
    elif (computer == 3):
        computer = "보"

    player = input("가위, 바위, 보 중에 하나 입력하세요! : ")
    while (player != "가위" and player != "바위" and player != "보"):
        player = input("가위, 바위, 보 중에만 하나를 입력하세요! : ")
    print("당신의 선택은 : "+player)
    print("컴퓨터의 선택은 : "+computer)

    if (player == computer):
        print("비겼어요~")
    elif (player == "바위"):
        if (computer == "보"):
            print ("이겼어요~")
        if (computer == "가위"):
            print ("졌어요~")
    elif (player == "보"):
        if (computer == "바위"):
            print ("이겼어요~")
        if (computer == "가위"):
            print ("졌어요~")
    elif (player == "가위"):
        if (computer == "바위"):
            print ("졌어요~")
        if (computer == "보"):
            print ("이겼어요~")