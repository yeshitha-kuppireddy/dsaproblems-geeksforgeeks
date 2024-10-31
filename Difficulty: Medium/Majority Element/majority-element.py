#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        s={}
        for i in arr:
            if i in s:
                s[i]+=1
            else:
                s[i]=1
        m=max(s, key=lambda k: s[k])
        return m if s[m]>len(arr)/2 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))
        print("~")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends