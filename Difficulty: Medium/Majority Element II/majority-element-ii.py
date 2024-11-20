class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)//3
        c={}
        a=[]
        for i in range(0,len(arr)):
            if arr[i] in c:
                c[arr[i]]+=1
            else:
                c[arr[i]]=1
        for j in c:
            if c[j] > n:
                a.append(j)
        return sorted(a)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends