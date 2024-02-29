import random

list = ['가위', '바위', '보']
user = 0
regame = 0
win = 0
defeat = 0
tie = 0


while regame != 'ㄴㄴ':
    computer = random.choice(list)
    user = input("가위, 바위, 보 중 하나를 선택하세요 : ")
    if user != '가위' and user != '바위' and user != '보':
        print('#유효한 입력이 아닙니다#')
        continue
    if user == computer:
        print('------무승부 입니다------')
        tie += 1
    elif user == '가위' and computer == '보' or user == '바위' and computer == '가위' or user == '보' and computer == '바위':
        print('------승리입니다------')
        win += 1
    else:
        print('-----패배 입니다-----')
        defeat += 1

    while regame != 'ㄴㄴ':
        regame = input('다시 하시겠습니까?(ㅇㅇ,ㄴㄴ) :')
        if regame != 'ㄴㄴ' and regame != 'ㅇㅇ':
            print('#유효한 입력이 아닙니다#')
        elif regame == 'ㄴㄴ':
            print('-----게임을 종료 합니다-----')
            print(f'승리 : {win} 패배 : {defeat} 무승수 : {tie}')
        else:
            break
