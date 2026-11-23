class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # return nums+nums

        """Another Approach : Running loop
        Time : O(n)
        Space: O(n)
        """
        n = len(nums)
        output = [0]*(2*n)

        # copy element of nums into output array
        for i in range(n):
            output[i] = nums[i]

        # Again copy element of nums into output array
        for i in range(n,2*n):
            output[i] = nums[i-n]

        return output

        