# 책 part2 그리디알고리즘
# 1이 될때 까지

n,k=map(int,input().split())
count=0

while True:
  #n이 k로 나눠지는 수가 되도록 한번에 빼기
  num=(n//k)*k
  count+=(n-num)
  n=num

  if n<k:
    break

  n//=k
  count+=1

#n이 1이 될때까지 1씩뺀횟수 합치기
count+=(n-1)
print(count)