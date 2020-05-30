# -*- coding: utf-8 -*-
# N명의 학생의 수학점수의 평균에 가장 가까운 사람을 구하시오

def result():
    N = int(input())
    n = list(map(int, input().split()))

    # round 함수는 소숫점 첫째자리에서 반올림
    avg = round(sum(n)/N)

    # 최소 비교값을 만들기 위해 필요한 변수
    min = 2147000000
    # 인덱스와 값을 동시에 할 수 있는 함수 (enumerate)
    for idx, x in enumerate(n):
        tmp = abs(x-avg)    #abs() 절대값을 구하는 함수
        if tmp < min:
            min = tmp       # 평균과의 절대값 차이를 줄이기 위해 사용
            score = x
            res = idx + 1   # index 는 0부터 시작해서 + 1
        elif tmp == min:    # 같은 값을 가지고 있을 때 점수가 높은 부분을 구하기 위해
            if x > score:
                score = x
                res = idx + 1

    print(avg, res)

if __name__ == '__main__':
    result()