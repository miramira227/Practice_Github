while True:
    print("가위바위보 중 하나를 선택하세요")

    if user =='가위':
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("무승부")
        elif random.choice(["가위", "바위", "보"]) == "바위":
            print("패")
        else:
            print("승")