def checkisap(arr,n):
   arr.sort()
   a=arr[1]-arr[0]
   for i in range(2,n-1):
      if arr[i+1]-arr[i]!=a:
        return False
   return True
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=checkisap(arr,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")

        
