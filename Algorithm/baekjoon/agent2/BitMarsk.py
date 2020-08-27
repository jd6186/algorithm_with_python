# 출처 : https://engkimbs.tistory.com/51

# n개의 꽉 찬 집합
n = 3
set = (1 << n) - 1


# 원소 추가
set |= (1 << n)

# 원소 포함 여부
set & (1 << n)

# 원소의 삭제
set &= ~(1<<n)

# 원소의 토글
set ^= (1<<n)

# 두 집합의 연산
added = (a | b); 
intersection = (a & b); 
removed = (a & ~b); 
toggled = (a ^ b);


# 집합의 크기
def bit_count(set, x):
    if(set == 0): 
        return 0 
    return x % 2 + bit_count( set / 2 )


sets = (1 << n); # 2에 3승

print(sets)