class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        """ Approach 1 : Run Two For Loops - Brute Force 
            Time : O(n^2) : Time Limit Exceeded
            Space : O(1)
        """
        # n = len(nums)
        # output = [0]*n
        # for i in  range(n):
        #     product = 1
        #     for j in range(n):
        #         if i != j:
        #             product *= nums[j]
        #     output[i] = product
        # return output

        """ Approach 2 : Using Auxiliary Space except output array
            Time : O(n)
            Space : O(n) excluding output array
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

        """ Approach 3: Modification in approach2 - without using Auxiliary [left and right] array
            Time : O(n)
            Space : O(1) excluding output array
        """
        n = len(nums)
        output = [1]*n

        # storing left product in output array
        for i in range(1,n):
            output[i] = output[i-1] * nums[i-1]
        print(output)

        right = 1 # its keep on accumulating product from right side 
        for i in range(n-1,-1,-1):
            output[i] *= right
            right *= nums[i]
        return output




        