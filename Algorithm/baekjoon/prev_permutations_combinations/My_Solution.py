# 패턴을 찾아보면 자기 포함 뒤에 존재하는 모든걸 끌고 자기 앞의 숫자를 제일 뒤로 보내면 된다.
    # 1 2 4 5 3 6
    # 1 2 4 3 6 5
    # 1 2 4 3 5 6
    # 1 2 3 6 5 4
    # 1 2 3 6 4 5
    # 1 2 3 5 6 4
    # 1 2 3 5 4 6
    # 1 2 3 4 6 5
    # 1 2 3 4 5 6
inputN = int(input())

inputL = list(map(int, input().split()))

def calc_Prev(inputL):
    
    # 1 2 4 5 3 6
    # 1 2 4 3 6 5
    # 1 2 4 3 5 6
    # 위 두가지 작동 방식이 서로 달라야한다.
    i = len(inputL)-1
    while i > 0 and inputL[i-1] < inputL[i]:
        i-=1
    
    if(i == 0):
        return False
    
    # 2가지 값만 바꿔도 되는 상황에서는 이것만 작동
    j = len(inputL)-1
    while inputL[i-1] < inputL[j]:
        j -= 1
    
    inputL[i-1], inputL[j] = inputL[j], inputL[i-1]
    
    # 3가지 값들을 서로서로 바꿔줘야 할 때 필요
    
    j = len(inputL)-1
    while i < j :
        inputL[i], inputL[j] = inputL[j], inputL[i]
        i += 1
        j -= 1
    
    return True

if(calc_Prev(inputL)):
    for i in range(len(inputL)):
        print(inputL[i], end=" ")
else : 
    print(-1)