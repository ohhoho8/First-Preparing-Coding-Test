#p.312 곱하기 혹은 더하기
num=input() #문자열로 입력받아 글자에 순서 부여받기
result=0 #곱하고 더하고 나서 최종적인 값
for i in num:
  if result==0 or eval(i)<=1: #현재 최종값이 0이거나 num값이 0 혹은 1일 때
    result+=eval(i) #더하기
  else: #최대한 많이 곱하는게 가장 큰 수가 나오므로
    result*=eval(i) #곱하기
print(result)
'''
1st input example 02984
1st output example 576

2nd input example 567
2nd output example 210
'''