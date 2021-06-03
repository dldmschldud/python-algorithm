# 책 part2 그리디알고리즘
# 1이 될때 까지

n,k=map(int,input().split())
count=0

#n>=k의 경우를 생각하지 않으면 n//k가 k보다 작아져서 n//k가 0이돼 무한루프에 빠질수 있다
#45//9
#5//9->0 무한루프에 빠지게됨

while n>=k:
 
  while n%k != 0:
    n-=1
    count+=1

  n//=k
  count+=1

while n>1:
  n-=1
  count+=1

print(count)
