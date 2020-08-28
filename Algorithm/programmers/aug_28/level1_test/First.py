def solution(n):
    arr = ["수"]
    for i in range(1, n):
        if(i %2 == 1):
            arr.append("박")
        else :
            arr.append("수")
    print("".join(arr))
    return 