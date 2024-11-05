def merge(arr1, arr2):
    merged = []
    i = j = 0
    inversion_count = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            # Count inversions: all remaining elements in arr1 after i are greater than arr2[j]
            inversion_count += len(arr1) - i
            j += 1

    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged, inversion_count

class Solution:
    def inversionCount(self, arr):
        # Helper function to implement merge sort and count inversions
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_inversions = merge_sort(arr[:mid])
            right, right_inversions = merge_sort(arr[mid:])
            merged, split_inversions = merge(left, right)

            # Total inversions are sum of left, right, and split inversions
            total_inversions = left_inversions + right_inversions + split_inversions
            return merged, total_inversions

        # Only the count of inversions is needed
        _, inversion_count = merge_sort(arr)
        return inversion_count

# Example usag\ # Output: 5


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends