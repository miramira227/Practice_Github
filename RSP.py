while True:
    print("가위바위보 중 하나를 선택하세요")

        if user=='보':
        if random.choice(["가위","바위","보"])=="가위":
            print("패")
        elif random.choice(["가위","바위","보"])=="바위":
            print("승")
        else:
            print("무승부")