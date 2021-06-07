t=int(input())

for i in range(t):
  n=int(input())
  data=list(map(int,input().split()))
  result=0
  data.sort()

  for j in range(2,n):
    result=max(result,abs(data[j]-data[j-2]))
  print(result) 