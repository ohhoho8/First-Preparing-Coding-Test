#p.315 볼링공 고르기 ~4:18
n, m=map(int, input().split())
balls=list(map(int, input().split()))
count=0
for i in range(n):
  for k in range(i+1,n):
    if balls[i]==balls[k]:
      continue
    count+=1
print(count)
'''
<excellent code>

n,m=map(int, input().split())
array=[0]*11 #1부터 10까지 무게를 담을 수 있는 리스트

for x in data:
  #각 무게에 해당하는 볼링공의 개수 카운트
  array[x]+=1

result=0
#1부터 m까지의 각 무게에 대하여 처리
for i in range(1,m+1):
  n-=array[i] #무게가 i인 볼링 공의 개수(A가 선택할 수 있는 개수) 제외
  result+=array[i]*n

print(result)
'''

'''
5 3
1 3 2 3 2
--> 8

8 5
1 5 4 3 2 4 5 2
--> 25
'''