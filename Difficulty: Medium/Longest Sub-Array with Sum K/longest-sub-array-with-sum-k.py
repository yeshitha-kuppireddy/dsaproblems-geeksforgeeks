# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        # code here
        count=0
        sum=0
        map={}
        for i in range(len(arr)):
            sum+=arr[i]
            if sum==k:
                count=i+1
            if sum-k in map:
                count=max(count,i-map.get(sum-k))
            if sum not in map:
                map[sum]=i
        return count



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