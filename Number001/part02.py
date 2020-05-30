# -*- coding: utf-8 -*-

import sys


def minNumber():
    # sys.stdin = open("part02_index.txt", "rt")

    T = int(input())

    for t in range(T):
        n, s, e, k = map(int, input().split())
        N = list(map(int, input().split()))
        N = N[s - 1: e]
        N.sort()

        print("#{},{}".format(t + 1, N[k - 1]))


if __name__ == '__main__':
    minNumber()
