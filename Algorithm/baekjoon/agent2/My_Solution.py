inputN = int(input())
arrI = [list(map(int, input().split())) for _ in range(inputN)]

def calc(a, inputN):
    
    # 유의사항 정리
    # 스타팅 포인트를 정해서 4가지 도시를 전부 도는 코드를 짠다.
    # 그럼 시작 지점에서 3개도시를 이동하고 마지막은 무조건 시작도시로 이동
    # 한번 갔던 도시는 가면 안된다.
    # 유의사항 마지막 도시에서는 시작도시로 돌아와야된다.
    
    # 각 스타팅별 도시 이동 비용 합산 값 모아주는 배열
    sumArr = []
    
    # 4개 도시 중 스타트 도시 지정해주기
    for k in range(inputN):
        
        # 여태까지 이동한 총 비용
        allCredit = []
        
        # 다음 이동 도시 이름
        nextCity = -1
        
        # 도시 4군데 돌기
        for i in range(inputN):
            # 다녀간 도시 목록
            cityArr = []
            # 다녀간 도시 목록에 시작 지점 등록
            cityArr.append(k)
            
            # 가장 저렴한 이동 가격
            minVal = 9999999
            
            # 마지막 도시에 도착했으면 스타트한 도시로 다시 되돌아가기
            if(i == inputN-1):
                ci = cityArr[0]
                
                # 이 때 비용을 allCredit에 append시켜주고
                allCredit.append(a[nextCity][ci])
                
                # 합산된 4개의 값을 합해주는 sum 함수를 이용해 sumArr에 그 값을 저장해주기
                sumArr.append(sum(allCredit))
            
            # nextCity가 없을 때
            if(nextCity == -1):
                # i도시에서 다른 도시로 이동할 때 가장 저렴한 곳 찾기
                for j in range(inputN):
                    
                    # 중요한건 길이 없거나 내 도시로는 못감 즉, 값이 0이면 못감
                    if(a[k][j] == 0):
                        continue
                    
                    # 이미 들렸던 도시라면 건너 뛰어야되니까 이렇게 체크
                    elif j in cityArr :
                        continue
                    
                    # 남은 도시들 중 값이 가장 저렴한 곳 찾기
                    # 남은 도시들을 배열에 담아 관리하기
                    else :
                        # i도시에서 j도시로 이동할 때 가격
                        val = a[k][j]
                        
                        # 이 가격이 minVal보다 저렴하다면 val이 minVal이다.
                        if(minVal > val):
                            minVal = val
                            
                            # 그리고 가장 저렴한 곳으로 이동해야되기 때문에 다음 도시로 j로 이동
                            nextCity = j
                
                # 그리고 가장 저렴했던 이동비들을 모아 합산해야됨으로 배열에 넣기
                allCredit.append(minVal)
            
            else : 
                
                # nextCity도시에서 다른 도시로 이동할 때 가장 저렴한 곳 찾기
                for j in range(inputN):
                    
                    # 중요한건 길이 없거나 내 도시로는 못감 즉, 값이 0이면 못감
                    if(a[nextCity][j] == 0):
                        continue
                    
                    # 이미 들렸던 도시라면 건너 뛰어야되니까 이렇게 체크
                    elif j in cityArr :
                        continue
                    
                    # 남은 도시들 중 값이 가장 저렴한 곳 찾기
                    # 남은 도시들을 배열에 담아 관리하기
                    else :
                        
                        # 이 도시에 들어왔으니까 다시는 못들어오게 등록
                        cityArr.append(nextCity)
                        
                        # i도시에서 j도시로 이동할 때 가격
                        val = a[nextCity][j]
                        
                        # 이 가격이 minVal보다 저렴하다면 val이 minVal이다.
                        if(minVal > val):
                            minVal = val
                            # 그리고 가장 저렴한 곳으로 이동해야되기 때문에 다음 도시로 j로 이동
                            nextCity = j
                        
                # 그리고 가장 저렴했던 이동비들을 모아 합산해야됨으로 배열에 넣기
                allCredit.append(minVal)
          
    # sumArr안에 있는 가장 작은 값 리턴해주기
    return min(sumArr)   

print(calc(arrI, inputN))