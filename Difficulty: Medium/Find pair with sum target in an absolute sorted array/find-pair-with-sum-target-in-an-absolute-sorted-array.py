#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    # Complete the below function
    def findPair(self,arr, target):
        dic = set()  # Using a set for faster lookups
        for i in arr:
            if (target - i) in dic:  # Check if the complement exists in the set
                return [target - i, i]  # Return the pair
            dic.add(i)  # Add the current element to the set
        return []
            
        # Your code here

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        res = ob.findPair(A, k)
        if len(res) == 0:
            print('[]', end="")
        else:
            # sort the output before printing
            res.sort()
            for i in range(len(res)):
                print(res[i], end=" ")        
        print("")
        print('~')
        T -= 1

if __name__ == "__main__":
    main()

# } Driver Code Ends