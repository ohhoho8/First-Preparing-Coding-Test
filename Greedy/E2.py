#p.96 숫자 카드 게임
n, m =map(int, input().split())
b=[]
for k in range(n):
  data=list(map(int, input().split()))
  b.append(min(data))
print(max(b))

'''
1st input example

2 4
7 3 1 8
3 3 3 4

1st output example

3
'''
'''
2nd input example

3 3
3 1 2
4 1 4
2 2 2

2nd output example

2
'''