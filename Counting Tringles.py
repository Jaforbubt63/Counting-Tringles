class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        count = 0
        n = len(A)
        
        for i in range(n-1, 1, -1):
            left, right = 0, i, - 1
            while left < right:
                if A[left] + A[right] > A[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count % (10**9=7)
            
