# LOTTERY
### lotto_main.py: 파일 실행 프로그램
### lotto.py: 함수들이 들어있음
- money_change_lotto: 금액을 입력하면 로또를 구매함
  - 이때, 문자열이나 로또 한장의 금액보다 작은 금액을 입력할 시 다시 입력
- input_lotto_number: 지난 주 당첨 로또 번호 6개를 입력
  - 중복되는 숫자, 6개가 아닌 숫자, 범위를 벗어나는 숫자를 입력할 경우 다시 입력
- generate_numbers: 리스트 안에 구매한 로또의 수 만큼의 1~45 숫자 중 랜덤으로 6개가 담긴 리스트를 넣어줌
- check: 몇등이 당첨되었는지 확인해줌
- view_result: 결과 출력 함수
- cal_money: 당첨금 계산 함수
- cal_yeild: 수익률 출력 함수