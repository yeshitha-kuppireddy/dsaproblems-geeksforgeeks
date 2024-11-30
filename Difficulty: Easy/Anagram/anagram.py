#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        s1=list(s1)
        s2=list(s2)
        s1.sort()
        s2.sort()
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends