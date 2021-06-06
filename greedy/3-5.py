#백준 그리디
#전자레인지 시간 구하기

n=int(input())
a=0
b=0
c=0
if n%10 != 0:
  print("-1")
else:
  
  a=n//300
  b=(n%300)//60
  c=((n%300)%60)//10

  print(a,b,c)


