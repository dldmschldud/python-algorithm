'''
n=int(input())
a,b=map(int,input().split())
data=list(map(int,input().split()))

print("n = ",n)
print("a = ",a)
print("b = ",b)
print(data)

'''
n=10
for i in range(n-1,-1,-1):
  print(i,end=" ")

print("")

for i in range(n-1,0,-1):
  print(i,end=" ")
