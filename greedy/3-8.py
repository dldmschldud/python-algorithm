#백준 그리디
#라디오주파수

a,b=map(int,input().split())
num=int(input())

a_b=abs(a-b)  #a에서b까지 감소or증가 버튼만 눌렀을 경우
data=list(range(num))

#각즐겨찾기 버튼을 눌렀을때, 즐겨찾기버튼은 무조건 한번만누름
for i in range(num):
  j=int(input())
  diff=abs(b-j)+1
  data[i]=diff

min_value=min(data)
print(min(a_b,min_value))