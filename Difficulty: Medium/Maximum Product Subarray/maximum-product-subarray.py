#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n=len(arr)
		res=float('-inf')
		l,r=0,0
		for i in range(0,n):
		    if l==0:
		        l=1
		    l=l*arr[i]
		    if r==0:
		        r=1
		    r=r*arr[n-1-i]
		    res=max(l,r,res)
		return res
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends