#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        for i in range(1,len(arr)+1):
            if arr[i-1]!=i:
                return i
        return i+1
         
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends