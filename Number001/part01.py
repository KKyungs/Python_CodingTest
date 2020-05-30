# -*- coding: utf-8 -*-


# 정수 n의 k 번째 약수를 찾는 코드

import sys


def divisor():
    # 파일에 있는 숫자를 불러오는 방법
    # sys.stdin = open("input.text", "rt")
    n, k = map(int, input().split())
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            print(i)
            break
    else:
        print(-1)


if __name__ == '__main__':
    divisor()
