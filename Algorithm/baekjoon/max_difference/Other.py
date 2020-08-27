# 10819번 차이를 최대로, 출처 : https://hooongs.tistory.com/204

import sys

# 다음 순열 찾는 함수
def nextseq(s):
    
    # 밑에 이미 sort를 오름차순으로 했기 때문에 더 큰 값이 없다는 것 자체가 배열이 끝났다는 뜻
    k = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            k = i

    if k == -1:
        return -1

    for j in range(k+1,len(s)):
        if s[j] > s[k]:
            m = j

    s[k], s[m] = s[m], s[k]
    tmp = s[k+1:]
    tmp.sort()

    return s[:k+1] + tmp

# main
n = int(input())
seq = [int(x) for x in sys.stdin.readline().split()]
seq.sort()      # 처음부터 탐색을 위해 오름차순 정렬

maxDis = 0
while True:
    sumDis = 0
    for i in range(len(seq)-1):
        sumDis += abs(seq[i+1] - seq[i])

    maxDis = max(maxDis, sumDis)
    
    seq = nextseq(seq)
    if seq == -1:
        break

print(maxDis)


# 이분은 할 때 배열의 값을 집어 넣으면서 전체 순열을 구해놓고 거기서 최대값을 찾는 형식으로 하셔서 나와같은 실수가 없으셨당