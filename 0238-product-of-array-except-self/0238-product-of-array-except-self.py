class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        """ Approach 1 : Run Two For Loops - Brute Force 
            Time : O(n^2)
            Space : O(1)
        """
        # n = len(nums)
        # output = [1]*n
        # for i in  range(n):
        #     product = 1
        #     for j in range(n):
        #         if nums[i] != nums[j]:
        #             product *= nums[j]
        #     output[i] = product
        # return output

        """ Approach 2 : Using Auxiliary Space except output array
            Time : O(n)
            Space : O(n)
        """
        n = len(nums)
        left = [1]*n
        right = [1]*n
        output = [1]*n

        # storing left product
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
         
        # storing right product
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        
        # output[i] = left[i] * right[i]
        for i in range(n):
                output[i] = left[i] * right[i] 
        return output

        