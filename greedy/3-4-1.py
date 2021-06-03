# 책 part2 그리디알고리즘
# 1이 될때 까지

n,k=map(int,input().split())
count=0

while n>=k:

  num=(n//k)*k
  count+=(n-num)
  n=num
  n//=k
  count+=1
  
count += (n-1)

print(count)
