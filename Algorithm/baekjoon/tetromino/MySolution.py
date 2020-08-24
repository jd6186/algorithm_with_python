import copy

N, M = map(int, input().split())

sdoquList =  []

for i in range(N):
    sdoquList.append(list(map(int, list(map(int, input().split())))))
    
# print(max(sdoquList))
# 이렇게 하면 각각의 첫 인덱스를 비교해서 가장큰 인덱스를 가진 배열을 도출해버린다.
# 따라서 각각의 최대 값을 찾아서 또 그것끼리 비교하는 것이 중요하다.

# 최대값을 구하고 값의 위치를 배열로 받아보자. python의 최대 장점을 이용해 for내부에 사용한 변수를 외부로 꺼내 사용해보자.
maxVal = 0
arrXY = [[], []]
for i in range(N):
    if(max(sdoquList[i]) > maxVal):
        arrXY = [[], []]
        maxVal = max(sdoquList[i])
        count = sdoquList[i].count(maxVal)
        sdoquListTest = copy.deepcopy(sdoquList)
        for j in range(count):
            arrXY[0].append(i)
            arrXY[1].append(sdoquListTest[i].index(maxVal))
            sdoquListTest[i].remove(sdoquListTest[i][sdoquListTest[i].index(maxVal)])
    # 많약 현재 최대값이 동일한 값들이 있을 수 있으니까 그 값들은 arrXY를 초기화하면 안되니까 따로 빼서 관리하자
    if(max(sdoquList[i]) == maxVal):
        count = sdoquList[i].count(maxVal)
        sdoquListTest = copy.deepcopy(sdoquList)
        for j in range(count):
            arrXY[0].append(i)
            arrXY[1].append(sdoquListTest[i].index(maxVal))
            sdoquListTest[i].remove(sdoquListTest[i][sdoquListTest[i].index(maxVal)])
        
            
# 값과 배열을 구했으면 이제 해당 값의 4방을 둘러서 가장 큰값쪽으로 이동해야지
# 해당 기능을 가진 함수를 만들어보자.
# 해당 값과 동일한 값이 배열 내에 있을 수 있으므로 
def choice_Val(sdoquList, arrXY):
    #테트로미노 원소 1개씩 넣는 곳
    
    #최종 4개 합산 결과값 넣는곳
    compareArr = []
    # 최대값이 여기저기 중복되었을 수 있으므로 for문을 만들어 중복됐던 값들 처리
    # resultArr의 2번째 원소를 구할 수 있다.
    ref_Val01 = [[], []]
    for j in range(len(arrXY[0])):
        x = arrXY[0][j]
        y = arrXY[1][j]
        resultArr = [sdoquList[x][y]]
        ref01 = 0
        if(TF(x-1, y)):
            ref01 = sdoquList[x-1][y]
            ref_Val01[0].append(x-1)
            ref_Val01[1].append(y)
        if (TF(x+1, y)):
            if(ref01 == sdoquList[x+1][y]):
                ref01 = sdoquList[x+1][y]
                ref_Val01[0].append(x+1)
                ref_Val01[1].append(y)
        elif(TF(x+1, y)):
            if(ref01 == sdoquList[x+1][y]):
                ref_Val01 = [[], []]
                ref01 = sdoquList[x+1][y]
                ref_Val01[0].append(x+1)
                ref_Val01[1].append(y)
        if (TF(x, y-1)):
            if(ref01 == sdoquList[x][y-1]):
                ref01 = sdoquList[x][y-1]
                ref_Val01[0].append(x)
                ref_Val01[1].append(y-1)
        elif(TF(x, y-1)):
            if(ref01 == sdoquList[x][y-1]):
                ref_Val01 = [[], []]
                ref01 = sdoquList[x][y-1]
                ref_Val01[0].append(x)
                ref_Val01[1].append(y-1)
        if (TF(x, y+1)):
            if(ref01 == sdoquList[x][y+1]):
                ref01 = sdoquList[x][y+1]
                ref_Val01[0].append(x)
                ref_Val01[1].append(y+1)
        elif(TF(x, y+1)):
            if(ref01 == sdoquList[x][y+1]):
                ref_Val01 = [[], []]
                ref01 = sdoquList[x][y+1]
                ref_Val01[0].append(x)
                ref_Val01[1].append(y+1)
        resultArr.append(ref01)
        
        # resultArr의 3번째 원소 구하기
        ref_Val02 = [[], []]
        for j in range(len(ref_Val01[0])):
            x = ref_Val01[0][j]
            y = ref_Val01[1][j]
            ref02 = 0
            if(TF(x-1, y)):
                ref02 = sdoquList[x-1][y]
                ref_Val02[0].append(x-1)
                ref_Val02[1].append(y)
            if (TF(x+1, y)):
                if(ref02 < sdoquList[x+1][y]):
                    ref02 = sdoquList[x+1][y]
                    ref_Val02[0].append(x+1)
                    ref_Val02[1].append(y)
            elif(TF(x+1, y)):
                if(ref02 < sdoquList[x+1][y]):
                    ref_Val02 = [[], []]
                    ref02 = sdoquList[x+1][y]
                    ref_Val02[0].append(x+1)
                    ref_Val02[1].append(y)
            if (TF(x, y+1)):
                if(ref02 < sdoquList[x][y+1]):
                    ref02 = sdoquList[x][y+1]
                    ref_Val02[0].append(x)
                    ref_Val02[1].append(y+1)
            elif(TF(x, y+1)):
                if(ref02 < sdoquList[x][y+1]):
                    ref_Val02 = [[], []]
                    ref02 = sdoquList[x][y+1]
                    ref_Val02[0].append(x)
                    ref_Val02[1].append(y+1)
            if (TF(x, y-1)):
                if(ref02 < sdoquList[x][y-1]):
                    ref02 = sdoquList[x][y-1]
                    ref_Val02[0].append(x)
                    ref_Val02[1].append(y-1)
            elif(TF(x, y-1)):
                if(ref02 < sdoquList[x][y-1]):
                    ref_Val02 = [[], []]
                    ref02 = sdoquList[x][y-1]
                    ref_Val02[0].append(x)
                    ref_Val02[1].append(y-1)
            resultArr.append(ref02)
            
            # resultArr의 4번째 원소 구하기
            ref_Val03 = [[], []]
            for j in range(len(ref_Val02[0])):
                x = ref_Val02[0][j]
                y = ref_Val02[1][j]
                ref03 = 0
                if(TF(x-1, y)):
                    ref03 = sdoquList[x-1][y]
                    ref_Val03[0].append(x-1)
                    ref_Val03[1].append(y)
                if (TF(x+1, y)):
                    if(ref03 == sdoquList[x+1][y]):
                        ref03 = sdoquList[x+1][y]
                        ref_Val03[0].append(x+1)
                        ref_Val03[1].append(y)
                elif(TF(x+1, y)):
                    if(ref03 == sdoquList[x+1][y]):
                        ref_Val03 = [[], []]
                        ref03 = sdoquList[x+1][y]
                        ref_Val03[0].append(x+1)
                        ref_Val03[1].append(y)
                if (TF(x, y-1)):
                    if(ref03 < sdoquList[x][y-1]):
                        ref03 = sdoquList[x][y-1]
                        ref_Val03[0].append(x)
                        ref_Val03[1].append(y-1)
                elif(TF(x, y-1)):
                    if(ref03 < sdoquList[x][y-1]):
                        ref_Val03 = [[], []]
                        ref03 = sdoquList[x][y-1]
                        ref_Val03[0].append(x)
                        ref_Val03[1].append(y-1)
                if (TF(x, y+1)):
                    if(ref03 == sdoquList[x][y+1]):
                        ref03 = sdoquList[x][y+1]
                        ref_Val03[0].append(x)
                        ref_Val03[1].append(y+1)
                elif(TF(x, y+1)):
                    if(ref03 == sdoquList[x][y+1]):
                        ref_Val03 = [[], []]
                        ref03 = sdoquList[x][y+1]
                        ref_Val03[0].append(x)
                        ref_Val03[1].append(y+1)
                resultArr.append(ref03)
                compareArr.append(sum(resultArr))
                del resultArr[3]
            del resultArr[2]
        del resultArr[1]
    return max(compareArr)

# IndexError 발생여부 판별용
def TF(x, y):
    try:
        sdoquList[x][y]
        return True
    except IndexError:
        return False

print(choice_Val(sdoquList, arrXY))