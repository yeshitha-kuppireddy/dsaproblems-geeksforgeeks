#User function Template for python3
 

class Solution:

    def kthSmallest(self, arr,k):
        me=arr[0:k]
        for i in arr[k:len(arr)]:
            if i<min(me):
                me.remove(max(me))
                me.append(i)
                #print(me)
            if i>min(me) and i<max(me):
                me.remove(max(me))
                me.append(i)
                #print(me)
        #print(me)
        return max(me)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends