#백준 그리디
#통나무 건너뛰기


t=int(input())

for i in range(t):
  n=int(input())
  data=list(map(int,input().split()))
  result=0
  data.sort() #데이터를 오름차순으로 정렬한후 제일 큰 수를 가운데에 놓고 큰수부터 차례대로 왼쪽 오른쪽에 놓아야 주어진 통나무로 최소 난이도를 만들수 있다
  #근데 실제로 데이터의 위치를 바꾸지 않고 [n]-[n-2]의 값중에서 최대값을 찾으면 됨

  for j in range(2,n):
    result=max(result,abs(data[j]-data[j-2]))
  print(result) 