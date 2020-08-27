import copy
num = int(input())

def calcP(num):
    arr = ["1 2 3", "1 3 2", "2 1 3", "2 3 1", "3 1 2", "3 2 1"]
    
    if(num == 1):
        return 1
    elif(num == 2):
        return ["1 2", "2 1"]
    elif(num == 3):
        return arr
    else : 
        for i in range(4, num+1):
            arrT = []
            for j in range(1, i+1):
                arrC = copy.deepcopy(arr)
                for z in range(len(arr)):
                    arrC[z] = arrC[z].replace(str(j), str(i))
                    arrT.append(str(j)+" "+arrC[z])
            arr = arrT
        arr.sort(key=None, reverse=False)
        return arr

if(num > 1):
    arrs = calcP(num)
    for count in range(len(arrs)):
        print(arrs[count])
        count += 1
else :
    print(calcP(num))