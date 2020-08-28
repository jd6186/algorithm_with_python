# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 맞았는데 시간초과... 다음에 도전하자

def solution(skill, skill_trees):
    answer = 0
    result = True
    for i in range(len(skill_trees)):
        arr = [0 for _ in range(len(skill))]
        print("몇번도니 : ", i+1)
        for j in range(len(skill_trees[i])):
            # skill 안에 있는 원소를 가지고 있는지 아닌지를 판단
            if(skill_trees[i][j] in skill):
                if(TF(arr, skill, skill_trees, i, j)):
                    print("오긴오니? : ", skill_trees[i])
                    result = True
                else :
                    result = False
        print("오긴오니?니 : ", skill_trees[i], "result? : ", result)
        if(result):
            print("누구니 : ", skill_trees[i])
            answer += 1   
    return answer


def TF(arr, skill, skill_trees, i ,j):
    one = skill_trees[i][j]
    for k in range(len(skill)):
        
        if(one == skill[k]):
            for z in range(k):
                print("skill_trees[i] : ", skill_trees[i], "arr[z] : ", arr[z])
                if(arr[z] == 0):
                    print("False됍니다. : ", skill_trees[i])
                    return False
            arr[k] = 1
            print("True됍니다. : ", skill_trees[i])
            return True

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
#가능한 스크리트리 개수