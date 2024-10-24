#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        marrnz=[]
        z=[]
        for i in range(0,len(arr)-1):
            if arr[i]==arr[i+1] and arr[i]!=0:
                marrnz.append(2*arr[i])
                arr[i+1]=0
            elif arr[i]!=arr[i+1] and arr[i]!=0:
                marrnz.append(arr[i])
            elif arr[i]==0:
                z.append(0)
        marrnz.append(arr[i+1])       
        return marrnz+z


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends