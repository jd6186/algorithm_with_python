refN = int(input())
inputNum = [int(input()) for _ in range(refN)]

result = 0
def calc(num):
    
    if(num == 1):
        return 1
    elif(num == 2):
        return 2
    elif(num == 3):
        return 4
    else :        
        arr = [1, 2, 4]
        ref = num - 3
        for i in range(ref):
            result = arr[0] + arr[1] + arr[2]
            arr[0] = result
            arr.sort(key=None, reverse=False)
        return  result

for j in range(refN):
    print(calc(inputNum[j]))
            