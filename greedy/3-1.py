# 책 part2 그리디알고리즘
# 거스름돈

n=int(input())
data=[500,100,50,10,5,1]
count=0

num=1000-n
for i in data:
  count+=num//i
  num=num%i

print(count)

