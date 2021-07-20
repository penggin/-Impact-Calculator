import time
from typing import Tuple

# 인자로 F(힘의 크기)(실수형), T(힘이 작용한 시간)(실수형) 을 받아서 실수형의 값을 리턴하는 delta_momentum (운동량의 변화량) 이라는 함수를 정의합니다.


def delta_momentum(F: float, T: float) -> float:
    dF = F * T  # 운동량의 변화량은 가해진 힘의 크기 X 힘이 가해진 시간 과 같습니다.
    return dF  # 계산한 값을 리턴합니다.


def calc_velocity(A: float, B: float, dF: float) -> Tuple[float, float]:
    Av = dF / A  # A 물체의 속력은 운동량의 변화량을 A의 질량으로 나눈것과 같다.
    Bv = dF / B  # B 물체의 속력은 운동량의 변화량을 B의 질량으로 나눈것과 같다.
    return Av, Bv  # 계산한 값들을 리턴한다.


def main():
    # 파이썬의 내장함수인 input() 를 이용하여 값을 입력받는다.
    # input() 함수는 괄호안의 내용을 출력하고, 사용자의 입력을 기다린다.
    A = float(input("A물체의 질량을 입력해주세요. (kg) : "))
    B = float(input("B물체의 질량을 입력해주세요. (kg) : "))
    F = float(input("충돌에서 작용한 총 힘의 크기를 입력해주세요. (N) : "))
    T = float(input("힘이 가해진 시간을 입력해주세요. (초) : "))

    # 위에서 만들어둔 운동량의 변화량을 구하는 함수를 이용하여, 운동량의 변화량을 구한후, dF에 넣는다.
    dF = delta_momentum(F, T)

    # 위에서 만들어둔 각 물체의 속력을 구하는 함수를 이용하여, 속력을 구한뒤, 각각 Av, Bv 에 넣는다.
    Av, Bv = calc_velocity(A, B, dF)

    # 결괏값들을 출력한다. 파이썬의 print() 함수는 괄호안의 내용을 출력한다.
    print(
        f"""
=========[입력값]==========
A 물체의 질량     : {A}
B 물체의 질량     : {B}
충돌에서 작용한 힘 : {F}
힘이 가해진 시간   : {T}
=========[출력값]==========
A 물체의 속도 : {Av}
B 물체의 속도 : {Bv}
"""
    )  # 파이썬에서 여러줄의 문자열을 표현할땐, """ 를 사용한다.
    while True:  # 무한히 반복한다.
        isrestart = input("다른 값을 계산하시겠습니까? (y/n) : ")
        if isrestart == 'y':  # 만약 isrestart 가 y 라면
            main()  # 메인함수를 다시 호출한다.
            return
        elif isrestart == 'n':  # 만약 isrestart 가 n 이라면
            print("프로그램이 종료됩니다...")  # 괄호안의 내용을 출력한다.
            time.sleep(2)  # 2초간 기다린다.
            return  # 함수를 탈출한다.
        else:  # 위의 조건이 모두 성립하지 않는다면
            continue  # 다시 반복한다.


main()
