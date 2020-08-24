# 오답인분들은 그냥 출처를 밝히지 않는게 더 나을 것 같아서 생략해놨습니당 ㅠㅠ

'''
# 풀이 1번
# 정리는 깔끔하게 했지만 이것조차 시간초과

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

di = [[0, 0, 0], [1, 2, 3], [0, 1, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, 1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 0, -1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [0, 1, 1], [0, 0, 1], [-1, -1, -2], [0, 0, -1], [1, 1, 2]]
dj = [[1, 2, 3], [0, 0, 0], [1, 0, 1], [0, 0, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, -1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 1, 1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [1, 2, 1], [0, 1, 0], [-1, -2, -1], [-1, 0, 0]]

max_sum = 0

for i in range(N):
    for j in range(M):
        for a in range(19):
            block_sum = area[i][j]
            for b in range(3):
                x = i + di[a][b]
                y = j + dj[a][b]
                if 0 <= x <= N-1 and 0 <= y <= M-1:
                    block_sum += area[x][y]
                else:
                    break
            else:
                if block_sum > max_sum:
                    max_sum = block_sum
print(max_sum)
'''

'''
# 풀이 2번
# 길지만 가장 브루트 포스를 잘 적용한 것 같은 코드 
# 하지만 그래 봤자 시간초과

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maplist = []
for i in range(N):
  maplist.append(list(map(int,input().split())))

dx = [[0,1,2,3],[0,1,0,1],[0,0,0,1],[0,0,1,1],[0,1,1,2]]
dy = [[0,0,0,0],[0,0,1,1],[0,1,2,2],[0,1,1,2],[0,0,1,0]]
convertedDx = [[0,-1,-2,-3],[0,-1,0,-1],[0,0,0,-1],[0,0,-1,-1],[0,-1,-1,-2]]
convertedDy = [[0,0,0,0],[0,0,-1,-1],[0,-1,-2,-2],[0,-1,-1,-2],[0,0,-1,0]]

rot = [[0,1],[0],[0,1,2,3,4,5,6,7],[0,1,4,5],[0,1,2,3]]


maxSum = 0
# cases of squares
for i in range(5):
  # iterate map
  for k in range(N):
    for l in range(M):
      # cases of rotation
      for j in range(len(rot[i])):
        curRot = rot[i][j]
        curDx = []
        curDy = []
        if curRot == 0:
          curDx = dx[i]
          curDy = dy[i]
        elif curRot == 1:
          curDx = convertedDy[i]
          curDy = dx[i]
        elif curRot == 2:
          curDx = convertedDx[i]
          curDy = convertedDy[i]
        elif curRot == 3:
          curDx = dy[i]
          curDy = convertedDx[i]
        elif curRot == 4:
          curDx = dx[i]
          curDy = convertedDy[i]
        elif curRot == 5:
          curDx = convertedDy[i]
          curDy = convertedDx[i]
        elif curRot == 6:
          curDx = convertedDx[i]
          curDy = dy[i]
        elif curRot == 7:
          curDx = dy[i]
          curDy = dx[i]
        
        if l+max(curDx) < M and k+max(curDy) < N and l+min(curDx) >=0 and k+min(curDy) >= 0:
          sumOfSquare = 0
          for p in range(4):
            sumOfSquare+=maplist[k+curDy[p]][l+curDx[p]]
          maxSum = max(sumOfSquare,maxSum)
print(maxSum)

'''

'''
# 풀이 3번 
# 전혀 다른 문제풀이 방식
# 응~ 그래봤자 시간초과~

import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

def check_shape(maps, shape):
    global answer
    y_length = len(maps) - len(shape)
    x_length = len(maps[0]) - len(shape[0])
    for start_y in range(y_length + 1):
        for start_x in range(x_length + 1):
            # 좌표 처음부터 순회
            value = 0
            for y in range(len(shape)):
                for x in range(len(shape[0])):
                    if shape[y][x] == 1:
                        value += maps[start_y + y][start_x + x]
            answer = max(answer, value)

def rotate(maps):
    return [list(reversed(i)) for i in list(map(list, zip(*maps)))]

line = [[1], [1], [1], [1]]
box = [[1,1], [1,1]]
shape1 = [[1,0], [1,0], [1,1]]
shape2 = [[1,0], [1,1], [0,1]]
shape3 = [[1,1,1], [0,1,0]]
shape4 = [[0,1], [0,1], [1,1]]
shape5 = [[0,1], [1,1], [1,0]]
shape_list = [line, box, shape1, shape2, shape3, shape4, shape5]

for shape in shape_list:
    if shape == line:
        for _ in range(2):
            check_shape(maps, shape)
            shape = rotate(shape)
        continue
    elif shape == box:
        check_shape(maps, shape)
        continue
    else:
        for _ in range(4):
            check_shape(maps, shape)
            shape = rotate(shape)
print(answer)
'''


# 풀이 4번 
# 풀이가 꼼꼼했던 분이라 자신감이 느껴졌었는데 역시나 통과되는 코드였네요 ^^
# 출처: https://jeongchul.tistory.com/670

# 값 입력받기
#저처럼 n,과 m을 우선 구분하셨고 그 후에 2중배열안에 값을 받으셨네요
# for _ in range(n) 이부분은 제가 보고 배워야되는 부분인것같아요 
# 배열 안에서  반복이 자동으로 되게 만드신게 아주 신박했습니다.
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]



# 이렇게 우선 테트로미노 모양들을 모두 정의를 하셨네요
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


# answer을 먼저 초기화 해주고
answer = 0

# 그 후 요구조건에 맞는 테트로미노를 찾아내는 함수를 만드셨고 특이한건 answer를 global변수로 만드셨더라구요 
# 이렇게 함으로서 solve에서 for문이 돌아도 전역변수기 때문에 다른 비교 필요없이 바로 바로 이전 코드의 최대값과 비교해 가장 큰 값을 찾아 줄 수 있어 효율적이네요
def find(x, y):
    global answer
    # 테트로미노의 총 개수가 19개라서 19번 도는 모습
    for i in range(19):
        result = 0
        # 조각은 4조각을 사용하므로 4번 돌면서 값을 찾는 구조네요
        for j in range(4):
            # 저와 마찬가지로 IndexError가 발생하면 그 부분에서 continue를 활용해 넘겨주신 모습 저는 if문에 사용될 거라 False를 반환했었죠
            try:
                next_x = x+tetromino[i][j][0] # x 좌표
                next_y = y+tetromino[i][j][1] # y 좌표
                # 각 조각이 1개씩 나올 때 마다 result에 더해주고 있는 모습
                result += board[next_x][next_y]
            except IndexError:
                continue
        # 방금 만들어진 result값과 기존의 answer을 비교해 더 큰 값을 answer로 지정해주고 있는 모습 이것도 기억해주도 좋을 코드 같아요
        answer = max(answer, result)

# 문제에서 주어진 n*m 칸에 맞게 틀을 구성해서 문제를 풀어주고 있는 모습
def solve():
    for i in range (n):
        for j in range(m):
            find(i, j)

# 해당 함수가 돌고 나면 answer의 값이 변경되겠죠?
solve()

# 전역변수인 answer을 출력해주면 결과값이 도출됩니다.
print(answer)
