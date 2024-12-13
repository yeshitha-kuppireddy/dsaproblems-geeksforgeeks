#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        c0,c1,c2=0,0,0
        for i in arr:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        #print(c0,c1,c2)
        i=0
        for j in range(c0):
            arr[j]=0
            i+=1
            #print(i)
        for j in range(i,i+c1):
            arr[j]=1
            i+=1
            #print(i)
        for j in range(i,i+c2):
            arr[j]=2
        return arr
            
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends