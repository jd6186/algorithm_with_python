# 입력값
#[1, 5, 2, 6, 3, 7, 4]
#[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 결과값
# [5, 6, 3]


def solution(array, commands):
    answer = []
    arr1 = array
    arr2 = commands
    answer = []
    i = 0
    while (i < len(arr2)):
        start = int(arr2[i][0])
        end = int(arr2[i][1])
        if(start == end):
            keyArr = arr1[start-1]
            answer.append(keyArr)
            i += 1
            continue
        keyArr = arr1[start-1:end]
        keyArr.sort()
        answer.append(keyArr[(int(arr2[i][2])-1)])
        i += 1
    return answer



'''
# 1등 풀이 단 2줄...
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 코드 분석
(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)
이게 람다 x는 commands인데 
sorted(array)를 할 때 
array를 우선 array[A:B]로 슬라이스 치고
그 다음 거기서 나온 값 중에 C에 해당하는 값 1개를 도출해내겠다!
여기서 map을 써서 람다 x를 키로 만들고 value는 commands로 했다는걸 기억해야됑
람다는 뒤에 식이오기 때문에 
lambda x : x가 사용될 식
형태로 표현하면 됑

lambda의 다른 표현식을 보면 
input = lambda: sys.stdin.readline().rstrip()
이런 식으로 lambda는 식을 동반한다는걸 잊지 말고 lambda로 정의된 건 하나의 메서드처럼 작동되기
때문에 나중에 저 변수를 다른 곳에서 사용하면 sys.stdin.readline().rstrip()이 값이 오는게 아니고
이 메서드가 사용되는 거라고 생각하면됑
'''