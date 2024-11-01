
class Solution:
    def findDuplicates(self, arr):
        # code here
        s=set()
        dp=[]
        for i in arr:
            if i in s:
                dp.append(i)
            else:
                s.add(i)
        return sorted(dp)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends