'''
# 가장 큰 값 / 가장 작은값 / 두번째로 큰값 / 두번째로 작은값  ...
num = int(input())
arr = list(map(int, input().split()))
arr.sort(key=None, reverse=True)

def calc(arr):
    if(num %2 ==0):
        nums = num / 2
    else :
        nums = ((num-1) / 2) + 1
    arrs = []
    for i in range(0, int(nums)):
        arrs.append(arr[i])
        if((num-i-1) > i):
            arrs.append(arr[num-i-1])
    
    maxVal = 0
    for j in range(len(arrs)-1):
        val = arrs[j] - arrs[j+1]
        maxVal = maxVal + abs(val)
    return maxVal

print(calc(arr))
'''

# 그냥 브루트 포스로 풀기
# 가능한 모든 순열 조합을 미리 만들고 그 모든 것들을 for문돌려서 가장 큰 값을 찾아내기     
# 다만 값이 중복되면 답이 나오지 않는다.

num = int(input())
arr = list(map(int, input().split()))

maxVal = 0

def calc(arrs, indexN):
    
    global maxVal
    if(num == 1):
        maxVal = 1
        return maxVal
    if(indexN == len(arr)):
        print(arrs)
        val = 0
        for j in range(len(arrs)-1):
            val = val + abs(arrs[j] - arrs[j+1])
            
        if(val > maxVal):
            maxVal = val
    else :
        for i in range (len(arr)):
            if arr[i] in arrs :
                continue
            else :
                calc(arrs+[arr[i]], indexN+1)
calc([], 0)    
print(maxVal)
