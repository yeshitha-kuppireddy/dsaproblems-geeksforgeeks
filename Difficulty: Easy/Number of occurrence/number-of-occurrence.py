class Solution:
    def countFreq(self, arr, target):
        #code here
        def cf(arr,target):
            if len(arr)==1:
                return 1 if arr[0]==target else 0
            if len(arr)==2:
                if arr[0]==target and arr[1]==target:
                    return 2
                elif (arr[0]==target and arr[1]!=target) or (arr[0]!=target and arr[1]==target):
                    return 1
                else:
                    return 0
            mid=len(arr)//2
            c=cf(arr[:mid],target)+cf(arr[mid:],target)
            return c
        return cf(arr,target)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends