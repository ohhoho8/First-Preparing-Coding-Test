#p.311 모험가 길드
number=int(input())
group=list(map(int, input().split()))
# 최대 그룹의 수를 구해야 하므로 오름차순으로 배치
group.sort()
count=0 #그룹의 수
index=0 #현재 그룹에 포함된 모험가의 수

for i in group:
  index+=1
  if index>=i: #공포도보다 모험가의 수가 크거나 같을 때
    count+=1 #그룹의 수 증가
    index=0 #현재 그룹에 포함된 모험가 수 초기화
print(count)
'''
1st input example
5
2 3 1 2 2

1st output example
2
'''