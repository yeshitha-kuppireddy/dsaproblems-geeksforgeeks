#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    # code here
	   if arr[0]==0:
	        return -1
	   maxreach=0
	   stepend=0
	   nj=0
	   for i in range(len(arr)-1):
	       maxreach=max(maxreach,arr[i]+i)
	       if stepend==i:
	           nj+=1
	           stepend=maxreach
	       if stepend>=len(arr)-1:
	           break
	   return nj if stepend >= len(arr) - 1 else -1
	    
	        
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends