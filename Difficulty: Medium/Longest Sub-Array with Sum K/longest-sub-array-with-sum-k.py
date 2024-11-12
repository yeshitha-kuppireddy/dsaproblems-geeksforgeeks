# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        # code here
        n=len(arr)
        hs={}
        s=0
        c=0
        for i in range(0,n):
            s+=arr[i]
            if s==k:
                c=max(c,i+1)
            if s-k in hs:
                c=max(c,i-hs[s-k])
            if s not in hs:
                hs[s]=i
        return c
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends