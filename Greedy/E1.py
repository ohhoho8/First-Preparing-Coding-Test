#p.92 큰 수의 법칙
n, m, k = map(int, input().split())
a=list(map(int, input().split()))
a.sort()
max_num=a[-1]
next_num=a[-2]
sum=0
for i in range(1,m+1):
  if i!=1 and i%k==1:
    sum+=next_num
  else:
    sum+=max_num
print(sum)

'''
1st input example

5 8 3
2 4 5 4 6

1st output example

46
'''