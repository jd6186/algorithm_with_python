def E(num):
    while(True):
        if(num > 15):
            num -= 15
            continue
        else : 
            return num

def S(num):
    while(True):
        if(num > 28):
            num -= 28
            continue
        else : 
            return num
    
def M(num):
    while(True):
        if(num > 19):
            num -= 19
            continue
        else : 
            return num

i = 1     
arr = list(map(int, input().split()))

while (True):
    numE = E(i)
    numS = S(i)
    numM = M(i)
    if(arr[0] == numE and arr[1] == numS and arr[2] == numM):
        break
    i += 1
    
print(i)
    
    
    
    
    
    
    