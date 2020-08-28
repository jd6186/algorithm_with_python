'''
# 조건정리

1. N개의 수와 N-1개의 연산자가 주어진다.
2. 덧셈, 뺄셈, 곱셈 나눗셈 연산자만 주어진다.
3. 나누기할 때 주의사항
    1) 나눗셈하고 남은 몫만 사용한다. 소수점이하는 버린다. 즉, int(10/6) 이런식으로하면 1만 남아야된다.
    2) 음수의 나눗셈은 음수를 양수로 바꾸고 해당 몫에 -를 붙여 음수를 만들어준다.
4. 연산자 우선순위를 무시하고 앞에서 부터 진행한다.
5. 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하라.

최대 최소값을 구하는 문제로 전체를 다 돌아서 문제를 해결해야하는 상황
깊이우선 탐색으로 하게되면  주어진 수하나와 관련된 모든 연산을 하나씩 처리해보고 오겠고
너비우선 탐색으로 하게되면 주어진 모든 수에 대한 내용을 전체 탐색하게 된다.

해당 문제에서는 모든 경우의 수를 다 탐색해야되므로 둘의 큰 차이는 없을 것으로 판단.
복습겸 DFS를 이용해 문제를 해결해보겠다.
'''
import copy

# 값 세팅
num = int(input())
arr = list(map(int, input().split()))
calcArr = list(map(int, input().split()))
# calcArr[0] = 덧셈,  calcArr[1] = 뺄셈,  calcArr[2] = 곱셈,  calcArr[3] = 나눗셈


# 연산자 세팅
def div(a, b):
    divi = int(abs(a) / b)
    if(a < 0):
        return -divi
    else : 
        return divi

copyCalc = copy.deepcopy(calcArr)
resultArr = []
copyArr = copy.deepcopy(arr)

def calc(startN, indexN, copyCalc):
    
    resultN = 0
    if(indexN == sum(calcArr)):
        return resultN
    else :
        # 반복회수는 copyCalc만큼 돌면서 하나의 연산자가 사용되면 하나씩 지워나가는 방식으로 진행하자.
        for i in range(sum(copyCalc)):
            print("sum(copyCalc) : ", sum(copyCalc), "i : ", i)
            # 반복회수는 copyCalc만큼 돌면서 하나의 인덱스가 
            for j in range(len(copyCalc)):
                print("len(copyCalc) : ", len(copyCalc), "j : ", j)
                if(copyCalc[0] == 0 and copyCalc[1] == 0 and copyCalc[2] == 0 and copyCalc[3] == 0):
                    print("모두 돌긴해? resultArr[len(resultArr)-1] : ", resultArr[len(resultArr)-1])
                if(copyCalc[j] > 0):
                    if(j == 0):
                        resultN = copyArr[startN] + arr[startN+1]
                        copyArr[startN+1] =resultN
                        resultArr.append(resultN)
                        copyCalc[j] -= 1
                        calc(startN+1, indexN+1, copyCalc)
                        copyCalc[j] += 1
                    elif(j == 1):
                        resultN = copyArr[startN] - arr[startN+1]
                        copyArr[startN+1] =resultN
                        copyCalc[j] -= 1
                        calc(startN+1, indexN+1, copyCalc)
                        copyCalc[j] += 1
                    elif(j == 2):
                        resultN = copyArr[startN] * arr[startN+1]
                        copyArr[startN+1] =resultN
                        copyCalc[j] -= 1
                        calc(startN+1, indexN+1, copyCalc)
                        copyCalc[j] += 1
                    else:
                        resultN = div(copyArr[startN], arr[startN+1])
                        copyArr[startN+1] =resultN
                        copyCalc[j] -= 1
                        calc(startN+1, indexN+1, copyCalc)
                        copyCalc[j] += 1
                else :
                    continue
                
        return resultArr
print(calc(0, 0, copyCalc))


