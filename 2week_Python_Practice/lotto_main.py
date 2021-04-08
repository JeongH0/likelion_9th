"""
로또 한장의 가격은 1000원입니다!
맨 처음 로또를 구매할 금액을 입력받을 수 있습니다.
구매한 금액에 따라 몇장의 로또를 구입을 하게 되는지 출력해주어야 합니다.
구매금액에 따른 로또들을 랜덤으로 자동생성을 하여 리스트 형태로 출력합니다.
이때 자동생성된 로또의 번호들은 정렬이 되어있어야 합니다.
로또의 번호는 1~45 까지로 제한합니다.
한 장의 로또는 6개의 숫자로 이루어집니다!
지난주 로또 번호를 입력받을 수 있습니다.
로또 담청 결과를 출력합니다.
자동으로 생성된 로또들과 지난주의 당첨번호를 비교하여 몇등이 당첨되었는지 알려줍니다.
수익률은 당첨된 금액 / 로또를 구입한 금액 으로 계산합니다.
"""
import lotto


purchase_lotto = lotto.money_change_lotto()
my_lotto_list = lotto.generate_numbers(purchase_lotto)

winning_number_list = lotto.input_lotto_number()

lotto_check_list = lotto.check(my_lotto_list, winning_number_list)

lotto.view_result(lotto_check_list)

money = lotto.cal_money(lotto_check_list)

lotto.cal_yeild(money, purchase_lotto)


