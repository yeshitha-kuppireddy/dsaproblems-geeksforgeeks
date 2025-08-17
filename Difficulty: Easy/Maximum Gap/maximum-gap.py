class Solution:
	def maxDiff(self, arr):
	    # code here
	    if not arr or len(arr)==1:
	        return 0
	    arr.sort()
	    return max([abs(arr[i]-arr[i+1]) for i in range(len(arr)-1)])
	    