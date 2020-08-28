def solution(x, n):
    answer = []
    z = x
    for i in range(n):
        answer.append(z)
        z = x * (i+2)
    return answer