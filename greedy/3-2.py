# 책 part2 그리디알고리즘
# 큰 수의 법칙

n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)

f=data[0] # 가장 큰수
s=data[1] # 두번째로 큰

count=m//(k+1) # 수열이 반복되는 횟수
result1=((f*k)+s)*count # 수열의 합
result2=(m%(k+1))*f # 나머지 합

print(result1+result2)
