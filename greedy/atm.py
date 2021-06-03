#백준 그리디
#atm
n=int(input())
data=list(map(int,input().split()))
result=0
data.sort(reverse=True)

for i in range(n):
  result+=(data[i]*(i+1))
 
print(result)
