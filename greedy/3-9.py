#백준 그리디
#값을 만들수 있는 최소 동전개수 구하기

n,k=map(int,input().split())
data=list(range(n))
count=0
for i in range(n):
  data[i]=int(input())

for i in range(n-1,-1,-1):
  count+=k//data[i]
  k%=data[i]

print(count)