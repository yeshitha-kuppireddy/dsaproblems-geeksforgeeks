#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        mins=arr[-1]-arr[0]
        #dp=arr
        for i in range(1,len(arr)):
            if arr[i]-k<0:
                continue
            mi=min(arr[0]+k,arr[i]-k)
            ma=max(arr[i-1]+k,arr[-1]-k)
            mins=min(ma-mi,mins)
            
        return mins


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends