import copy

inputN = int(input())
inputL = list(map(str, input().split()))
inputS = " ".join(inputL)

# 3의 순열 조합
br_F = ["1 2 3", "1 3 2", "2 1 3", "2 3 1", "3 1 2", "3 2 1"]

if(inputN < 4):
    if(inputN == 1):
        print(-1)
    if(inputN == 2):
        if(inputS == "1 2"):
            print("2 1")
        else :
            print(-1)
    if(inputN == 3):
        indexNum = br_F.index(inputS)
        if(indexNum+1 == len(br_F)):
            print(-1)
        else :
            print(br_F[indexNum+1])
            
else :
    def calc_PC(inputN):
        br_T = []
        for z in range(4, inputN+1):
            for i in range(1, z+1):
                for j in range(len(br_F)):
                    temp = copy.deepcopy(br_F)
                    if(br_F[j].find(str(i)) >= 0):
                        temp[j] = temp[j].replace(str(i), str(z))
                    br_T.append(str(i) + " " + temp[j])
            br_F = br_T
            br_T = []
        br_F.sort(key=None, reverse=False)
        return br_F

    s_List = calc_PC(inputN)
    indexNum = s_List.index(inputS)
    if(indexNum+1 == len(s_List)):
        print(-1)
    else :
        print(s_List[indexNum+1])