from random import randint
LOTTO_PRICE = 1000          # 로또 한장의 가격
WINNING_PRICE = [5000000, 100000, 20000, 5000]      # 1등~4등까지의 당첨금
WINNING_CONDITION = [6, 5, 4, 3]        # 당첨 조건


def money_change_lotto():       # 문자열을 입력받거나, 한장의 가격보다 낮은 금액을 입력 받을 시, 다시 입력
    """
    :return: 구매한 로또 용지의 개수
    """
    while True:
        input_money = input("> 구입금액을 입력해 주세요.\n ")
        if input_money.isalpha():
            print("> 숫자를 입력해주세요")
        elif int(input_money) < LOTTO_PRICE:
            print("> 로또의 최소 가격은 {}원 입니다.".format(LOTTO_PRICE))
        else:
            purchase_lotto = int(input_money) // LOTTO_PRICE
            print("> {}장의 로또를 구입하셨습니다.".format(purchase_lotto))
            return purchase_lotto

def input_lotto_number():
    """
    :return: 지난 주 당첨 로또 번호 6개
    """
    while True:
        check_overlap = 0       # 중복 확인을 위한 장치
        lotto_num_list = [int(num) for num in input(">지난주 당첨 번호를 입력해주세요\n").split(",")]
        lotto_num_list.sort()

        for i in range(len(lotto_num_list) - 1):
            if lotto_num_list[i] == lotto_num_list[i + 1]:      # 정렬 된 상태에서 리스트의 n번째와 n+1번째가 같은 것을 비교하는게 in 보다 더 효율적이라 판단.
                check_overlap = -1
                break

        if len(lotto_num_list) != 6:
            print("> 로또는 6개의 숫자로 이루어집니다.")
        elif lotto_num_list[0] < 1 or lotto_num_list[-1] > 45:
            print("> 1~45까지의 숫자를 입력해주세요.")
        elif check_overlap == -1:
            print("> 중복되는 숫자를 제거해주세요.")
        else:
            return lotto_num_list


def generate_numbers(purchase_lotto):
    """
    :param purchase_lotto: 구매한 로또 용지의 개수
    :return: 1~45 숫자들이 들어있는 구매한 로또들의 리스트
    """
    my_lotto_list = []      # 로또 번호들이 담길 리스트

    for i in range(purchase_lotto):
        lotto_num_list = []
        while len(lotto_num_list) < 6:
            number = randint(1, 45)             # 중복 제거
            if number not in lotto_num_list:
                lotto_num_list.append(number)
        lotto_num_list.sort()
        print(lotto_num_list)
        my_lotto_list.append(lotto_num_list)        # 생성된 로또 번호 6개를 리스트에 넣어줌 (로또 용지 1장과 같은 원리)

    return my_lotto_list

def check(my_lotto_list, winning_number_list):
    """
    :param my_lotto_list: 내가 구매한 로또
    :param winning_number_list: 당첨 로또 리스트
    :return: 몇등이 당첨되었는지 확인해주는 리스트
    """

    lotto_check_list = [0,0,0,0]        # 1등, 2등, 3등, 4등 순서

    for lotto_paper in my_lotto_list:
        count = 0
        for number in lotto_paper:          # 로또 용지들의 숫자들이 당첨과 같을때마다 count 1씩 증가
            if number in winning_number_list:
                count += 1
        if count == WINNING_CONDITION[0]:       # count 가 각각 등 수의 조건과 같을 경우, 그 등수에 해당하는 리스트의 숫자 1 증가
            lotto_check_list[0] += 1
        elif count == WINNING_CONDITION[1]:
            lotto_check_list[1] += 1
        elif count == WINNING_CONDITION[2]:
            lotto_check_list[2] += 1
        elif count == WINNING_CONDITION[3]:
            lotto_check_list[3] += 1

    return lotto_check_list

def view_result(lotto_check_list):      # 결과 출력 함수
    print("> 로또 당첨 결과")
    for i in range(3, -1, -1):
        print("{}등({}개가 맞을 때) - {}원 - {}개".format(i + 1, WINNING_CONDITION[i], WINNING_PRICE[i], lotto_check_list[i]))

def cal_money(lotto_check_list):        # 총 수익금 계산 함수
    money = 0
    for i in range(len(lotto_check_list)):
        money += lotto_check_list[i] * WINNING_PRICE[i]

    return money

def cal_yeild(money, purchase_lotto):       # 수익률 계산 함수
    """
    수익률은 총 이익금 / 투자 원금
    purchase_lotto 즉, 구매한 로또용지의 개수를 받는 이유는 구입금액은 1000원 단위로 절삭되는데, 이때 포함되지 않은 백원 이하의 금액을
    포함할 경우 원금이 아니게됨.
    """
    print("> 수익률")
    print("{}배".format(money / (purchase_lotto * 1000)))




