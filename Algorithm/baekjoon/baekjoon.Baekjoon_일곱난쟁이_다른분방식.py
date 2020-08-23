# 출처 : https://daimhada.tistory.com/163

arr = []
# 값 받기 
for i in range(9):
    arr.append(int(input()))

# 값 계산하기 이부분이 중요! 7명을 계산해서 100을 만들어 내는게 아니고 
# 전체 합값에서 2명을 빼서 100이나오는 것을 찾는거야 이후 코드를 보자
res = sum(arr)


# 배열 순환하며 값찾기 인자가 2개밖에 없으므로 2중 for문이면 가능하다.
for i in range(9):
    for j in range(i+1, 9):
        if(res - arr[i] - arr[j] == 100):
            #여기서 나온 for문은 그냥 문자 출력용 for문
            for k in range(9):
                if(k == i or k == j):
                    continue
                else :
                    print(arr[k])
        