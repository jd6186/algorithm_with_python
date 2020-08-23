# 풀이 1번 => 실패
# 

# i = 0
# arr = []
# arrTest = []
# while(i < 9):
#   if(len(arr) == 7):
#       j = 0
#       for j in range(0, len(arr), 1):
#           addNum = int(input())
#           arr[j] = addNum
#           if(arr.sums() == 100):
#               return arr
#           else:
#               continue          
#                     
#   arr.append(int(input()))
#   if(len(arr) >= 7):
#     if(arr.sums == 100):
#       return arr
#     elif(): 
#         continue

    
    
# 풀이 2번
# 
# i = 0
# arr = []
# # 값 받기
# for i in range(0, 9, 1):
#     arr.append(int(input()))
# 
# # 값 정렬
# arr.sort(key=None, reverse=True)
# 
# # 값 분석
# for j in range(0, 3, 1):
#     print("몇 회차니? : ", j)
#     arrT = [arr[j]]
#     sums = arr[j]
#     k = j+1
#     while(True):
#         print("몇 회차니? : ", j, " 그리고  ", k+6)
#         if(k+6 > len(arr)):
#             break
#         for z in range(k, k+6, 1):
#             sums = sums + arr[z]
#             arrT.append(arr[z])
#         print(sums)
#         if(sums != 100):
#             arrT = [arr[j]]
#             sums = arr[j]
#             k += 1
#             continue
#         elif(sums == 100) :
#             print("결과값 : ",arrT)
#             break
#     if(sums == 100):
#         break
#     else :
#         continue




# 풀이 3번 브루트 포스를 이용한 알고리즘으로 문제 풀기
# 일부 지점만 구간 반복하는 것이 아니라 전체영역을 반복하며 돌기
# arr = []
# # 값 받기
# for i in range(0, 9, 1):
#     arr.append(int(input()))
#     
# # 7 난쟁이 넣기
# def nanSum(arr) :
#     nan = []
#     a = 0
#     for i in range(a, a+7, 1):
#             
#         
# # for문 돌려서 값 7개 합산하기             
# def forLoop(arr):
#     sum = 0
#     for i in range(0, 7, 1):
#         sum = sum + arr[i]
#     return sum 

# 아무리 뇌로 시물레이션 돌려도 답이 안나오는데 코드를 칠 수가 없다.



