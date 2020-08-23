'''
# 문제 정리
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성하라

입력값
[3, 0, 6, 1, 5]

결과 값
3

'''

################################################################################################################################

# 문제 풀이 (난 내 풀이가 가장 맘에 드는데?)

citations = [3, 0, 6, 1, 5, 3, 3, 5, 7, 5, 10]

def solution(citations):
    answer = 0
    arr = []
    #전체 논문의 개수
    n = len(citations)
    #h번 이상 인용된 논문을 쉽게 구하기 위해 sorting
    #앞으로 내 뒤에 나올 논문은 나와 같거나 나 이상으로 인용된 논문이 되게 만든 것
    citations.sort()
    print("sorting까지는 되어있어 ", citations)
    i = 0
    while(i < n):
        # h = i+1번째 논문의 인용회수
        h = citations[i]
        # 위에 남은 논문의 개수 = n-i개
        if(h <= (n - i)):
            # 나머지 논문이므로 지금 논문을 제외해야되서 i+1이 아닌 그냥 i
            if(h >= i):
                arr.append(h)
        # 중복되는 숫자는 건너뛰고 다음 숫자를 봐야함으로 건너 뛰기 구현
        count = 0
        if(i+1 < n):
            if(citations[i] == citations[i+1]):
                low = i
                hi = i+1
                while(citations[low] == citations[hi]):
                    if(citations[low] == citations[hi]):
                      count += 1
                    low += 1
                    hi += 1
                i += 1 + count
                if(i >= n):
                  break
                continue
        i += 1
    answer = max(arr)
    print(arr)
    return answer

print(solution(citations))