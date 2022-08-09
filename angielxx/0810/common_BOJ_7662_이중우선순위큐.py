# BOJ 7662 이중 우선순위 큐
# 220809

"""
-45 653
-653 45
D 1일때만 max_Q로 전환시켜서 최소값 삭제한 다음에,
max_Q를 하나씩 순회하며 새로 리스트에 넣어 Q를 다시 만든다.
"""
import heapq

T = int(input())

for _ in range(T):
    k = int(input())

    # 최소힙 : +로 숫자 넣고, 가장 작은 숫자 heapqpop
    min_Q = []

    for _ in range(k):
        A, N = input().split()
        N = int(N)

        # I라면 heapqpush
        if A == 'I':
            heapq.heappush(min_Q, N)
        # D라면
        else:
            # min_Q에 
            if min_Q:
                if N == -1:
                    heapq.heappop(min_Q)
                    # print('2', min_Q)
                else:
                    # max_Q 재정의
                    max_Q = []
                    for num in min_Q:
                        heapq.heappush(max_Q, num * -1)  # 오답! heappush로 안 넣으니까 우선순위 큐로 삭제가 안됨
                    heapq.heappop(max_Q)
                    
                    # min_Q 재정의
                    min_Q = []
                    for num in max_Q:
                        heapq.heappush(min_Q, num * -1)

    if min_Q:
        print(min_Q[-1], min_Q[0])
    else:
        print('EMPTY')