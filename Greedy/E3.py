#p.99 1이 될 때까지
n, k = map(int, input().split())
count=0
while True:
  if n==1:
    break
  elif n%k==0:
    n=n//k
    count+=1
  else:
    n-=1
    count+=1
print(count)
'''
1st input example : 25 5
    output example : 2

2nd input example : 25 3
    output example : 6
'''
'''
***Excellent answer***
# N , K 를 공백으로 구분하여 입력받기
n, k =map(int, input().split())
result = 0

while True:
  # (N == K 로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # K로 나누기
  result += 1
  n // = k

# 마지막으로 남은 수에 대하여 1씩 빼기
result ++ (n - 1)
print(result)
'''