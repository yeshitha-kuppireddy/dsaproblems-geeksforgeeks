
class Solution:
    def trappingWater(self, arr):
        '''cm=min(arr[0],arr[-1])*(len(arr)-2)
        for i in arr[1:len(arr)-1]:
            if i<max(arr[-1],arr[0]):
                cm-=i
            else:
                cm+=i
        return cm'''
        left, right = 0, len(arr) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
    
        while left < right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water_trapped += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water_trapped += right_max - arr[right]
                right -= 1
    
        return water_trapped
            

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends