

# Find the maximum for each and every contiguous subarray of size K
 
def printMax(arr, N, K):
    max = 0

    for i in range(N - K + 1):
        max = arr[i]
        for j in range(1, K):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end="")



arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
K = 3
    
# Function call
printMax(arr, N, K)
    
