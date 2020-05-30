# -*- coding: utf-8 -*-

# k번 쨰 큰 수 구하는 식

def big():
    # N 과 K 입력
    N, K = map(int, input().split())

    # n은 N의 리스트 원소값
    n = list(map(int, input().split()))

    # 중복값을 방지하기 위해 set() 자료구조를 사용
    res = set()

    for i in range(N):
        for j in range(i + 1, N):
            for m in range(j + 1, N):
                res.add(n[i] + n[j] + n[m])
    # set() 형식은 sort() 정렬을 사용할 수 없어 리스트형식으로 변환
    res = list(res)
    # 내림차순으로 정렬
    res.sort(reverse=True)

    # 리스트 형식이라 인덱스가 0부터 시작해서 -1을 해줌
    print(res[K - 1])


if __name__ == '__main__':
    big()
