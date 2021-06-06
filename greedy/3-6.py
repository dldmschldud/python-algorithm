#백준 그리디
#통나무 건너기

#테스트 케이스 개수
num=int(input())

for i in range(num):
  #통나무 개수
  n=int(input())
  data=list(map(int,input().split()))
  data.sort(reverse=True)

  #최대값을 가운데에 놓고 차례차례 왼쪽 오른쪽 번갈아서 놓기
  tmp=data[0]
  data[0]=data[1]
  data[1]=tmp
 

  max_value=abs(data[0]-data[n-1])

  for j in range(n-1):
    if max_value<abs(data[j]-data[j+1]):

      max_value=abs(data[j]-data[j+1])

  print(max_value)
  
  