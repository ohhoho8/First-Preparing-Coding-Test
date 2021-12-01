#p.314 만들 수 없는 금액
#실패
from itertools import combinations

num=int(input())
coins=list(map(int, input().split()))
possible=set()
result=[]
for k in range(num):
  result=[]
  result=list((combinations(coins, k+1)))
  possible.add(sum(result[a]) for a in range(num))
impossible={n for n in range(1, sum(coins)+1) if n not in possible}
print(min(impossible))