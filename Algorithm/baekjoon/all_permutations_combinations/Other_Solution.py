# 출처 : https://home-body.tistory.com/261

def permutations(selected, k):
    if k == N:
        print(' '.join(list(map(str, selected))))
    else:
        for i in range(1, N+1):
            if i not in selected:
                permutations(selected+[i], k+1)

N = int(input())
permutations([], 0)