
'''﻿
몇개의 숫자가 주어지든 결국 6개짜리 조합을 만들어야한다.
그 말인즉슨 최소 6이상의 숫자들이 들어올 것이고
49 이하의 숫자로 이루어져있기 때문에 최대 숫자는 49개 밖에 안된다.
어째든 배열의 첫번째 숫자는 총 개수를 의미하고 인덱스 1번 부터가 진짜 내가 고른 숫자들이다.
그럼 한번 내가 고른 숫자는 다시 사용하면 안되므로 이것 또한 비트마스크를 씌워 계산하면 금방 끝나겠다.
'''

# Setting 영역입니다.
arr = []
# 배열에 들어온 값들을 2중 배열에 담아주기
# 0이나올 때까지 계속 반복
while (True):
    inp = list(map(int, input().split()))
    if(len(inp) == 1 and inp[0] == 0):
        break
    arr.append(inp)

# 배열의 길이들만 담는 1차원 배열
inputN = []

# 배열들을 실제 담아줄 2차원 배열
arrL = []

# 만든 배열에 값을 옮겨줄 반복문
for i in range(len(arr)):
    inputN.append(arr[i][0])
    arrL.append(arr[i][1:])

# 비트마스크 세팅해두기
bitMarsk = [[0] * inputN[_] for _ in range(len(arrL))]

# 여기까지 세팅 끝
###########################################################################


# 계산하는 영역입니다.

# 6자리 숫자 조합을 구할건데 중복되는 값이 있으면 안됑
# 그러니까 6번째 반복이되서 값을 표출할 부분이 되면 arrR배열안에 담고  담을 때도 만약 arrR안에 이미 해당 값이 있으면 못담게 만들어

# count = 해당 배열의 길이는?, 인자값을 담아줄 배열, 몇번 돌았는지 알려줄 indN
arrR = []
def calc(k, count, ar, indN, useN):
    global arrR
    if indN == 6 :
        useN.sort()
        # 모든 경우의 수를 다 만들거라서 이미 있는 배열이 있을 수 있다. 그럴 땐 들어가면 안되므로 if문으로 구별
        if useN in arrR:
            print("이미 값이 들어있습니다.")
        else :
            arrR.append(useN)
        return
    
    # 비트마스크를 이용해서 각 값을 단 1번만 사용한 6자리 숫자조합을 만들어라!!
    # 틀만 짜주면
    else : 
        for i in range(indN, count): # 총 반복회수는 8개든 9개든 돌면서 값을 찾아야지
            if(bitMarsk[k][i] == 0):
                bitMarsk[k][i] = 1
                calc(k, count, ar, indN+1, useN+[ar[i]])
                useN = useN[:(len(useN))]
                bitMarsk[k][i] = 0
            else : 
                print("비트마스크에 1이라고 체크되었네용~ : ")
                continue

# arrR이 새롭게 시작할 수 있게 arrR의 값을 담아주는 배열
printArr = []

# arrR안에 출력할 요소들을 담아주는 반복문
for k in range(len(arrL)):
    calc(k, inputN[k], arrL[k], 0, [])
    arrR.append([""])
    printArr = printArr + arrR
    arrR = []
    
# 실제 출력을 하는 반복문
for i in range (len(printArr)):
    result = list(map(str, printArr[i]))
    print(" ".join(result))