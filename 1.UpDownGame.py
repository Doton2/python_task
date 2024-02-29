import random

random_number = random.randint(1,3)

count = 0
before_count = 0
input_number = 0

print('Up Down Game')
while random_number != input_number:
    try:
        input_number = int(input('1 ~ 100 까지 숫자를 입력하세요 :'))
    except:
        print('유효한 숫자를 입력하세요')
        continue
    if input_number > 100 or input_number <= 0:
        print('유효한 숫자를 입력하세요:')
    elif input_number == random_number:
        count +=1
        print('정답입니다.')
        print(f'시도한 횟수{count} 입니다.')
        if before_count <= count:  # 이전 최고 시도 횟수 저장
            before_count = count
        while True: # 다시 게임 여부 질문
            try:
                re_game = input('다시 하시겠습니까? (y/n) : ')
                if re_game.lower() != 'y' and re_game.lower() != 'n':
                    print('Y or N를 입력하세요')
            except:
                continue
            if re_game.lower() == 'y':
                print(f'이전 게임 플레이어 최고 시도 횟수:{before_count}')
                count = 0
                input_number=0
                random_number = random.randint(1,3)
                break
            elif re_game.lower() == 'n':
                count = 0
                break
    elif input_number > random_number:
        print('Down')
        count +=1
    elif input_number < random_number:
        print('Up')
        count +=1