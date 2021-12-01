#p.313 문자열 뒤집기
num=input()
#앞뒤 다른 숫자가 오면 index 리스트에 추가
index=[i for i in range(len(num)) if num[i]!=num[i-1]]
index.append(len(num)) #마지막 위치 추가
print(len(index)//2) #앞뒤 숫자 다른 위치 수를 2로 나누기
#//를 사용해야 최선의 경우의 수가 나온다
'''
1st input example
0001100
1st ouput example
1

2nd input example
01101101100
2nd output example
3
'''