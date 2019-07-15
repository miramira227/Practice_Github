import random
while True:
    if user=='바위':
        if random.choice(["가위","바위","보"]=="가위"):
            print("승")
        elif random.choice(["가위","바위","보"]=="바위"):
            print("무승부")
        else:
            print("패")