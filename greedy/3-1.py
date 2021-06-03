# 책 part2 그리디알고리즘
# 거스름돈

n=int(input())
data=list(map(int,input().split()))
count=0

for i in data:
  count+=n//i
  n=n%i

print(count)

