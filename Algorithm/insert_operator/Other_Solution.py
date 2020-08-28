N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)

# 내코드와 가장 큰 차이점은 연산자를 배열에 받아계산했냐 안했냐인데
# 이게 문제가 됐던 부분이 실제 그 값이 바뀌어버려서 1번만 돌 때는 상관이 없는데 2번 3번돌면 다른 연산에서 바뀐 값이 적용되어버렸단 겁니다.
# 이렇게 심플하게 구할 수 있다니 이해도 쉽고 가독성도 높아서 좋았습니다.