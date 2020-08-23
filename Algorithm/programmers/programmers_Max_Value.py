# 문제 정리

# [6, 10, 2]가 입려되면 만들 수 있는 수는?
# [6102, 6210, 1062, 1026, 2610, 2106]
# "6210"

# 문제는 이런 형태로 나올 때야...
# [3, 30, 34, 5, 9]     이걸 그냥 sort시키면 34303이 나와버리거든 근데 중요한건 9534330이게 더 크단거지
# "9534330"

# [100, 1, 11, 1111, 1000, 11]
# "1111111111001000"

# 이중 가장 큰 값은? 6210
# 이걸 문자열로 출력
# return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


############################################################################################################################3333

# 풀이 시작

numbers = [6102, 6210, 1062, 1026, 2610, 2106]

"""
# 내가 푼 방식

def myQuickSort(nums, L, H):
    if L >= H:
        return 

    # pos를 진행하면서 l에서 r까지의 범위가 정렬이 됨 (우선순위 가장 작은게 맨 뒤로 감)
    # pos는 nums에서 가장 우선순위가 작은 값 
    pos = partition(nums, L, H)

    # QuickSort는 pos(우선선위가 가장 작은 값)
    myQuickSort(nums, L, pos-1)
    myQuickSort(nums, pos+1, H)

def partition(nums, L, H):
    # print(nums, l, r)
    low = L
    while L < H:
        # l + r > r + l 이면 
        if compare(nums[L], nums[H]):
            nums[L], nums[low] = nums[low], nums[L]
            low += 1

        L += 1

    # 가장 낮은 순위 low를 가장 오른쪽 r과 변경 
    # 여기서 r은 분할정복으로 들어왔기에 들어온 값중에서 마지막임 
    nums[low], nums[H] = nums[H], nums[low]
    return low

def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def solution(numbers):
    myQuickSort(numbers, 0, len(numbers)-1)
    answer = str(int("".join(map(str, numbers))))
    return answer
"""

# 1등 문제풀이

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

    
print(solution(numbers))