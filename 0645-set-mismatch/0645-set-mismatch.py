class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        """ Approach1 : Using Frequency Array 
            Time : O(n)
            Space : O(n)
        """
        n = len(nums)
        freq = [0]*(n+1)  # accessing array from index 1

        # building frequency array
        for i in range(len(nums)):
            freq[nums[i]] += 1

        duplicate = -1
        missing = -1
        for i in range(1,n+1):
            if freq[i] == 2:
                duplicate = i
            if freq[i] == 0:
                missing = i
        return [duplicate,missing]

  

        """ Approach2 : Using Same nums array [Negation Method]
            Time : O(n)
            Space : O(1)
        """

        duplicate = -1
        # Finding duplicate
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num - 1 # array index start with 0

            if nums[idx] < 0:
                duplicate = num
            else:
                nums[idx] = -nums[idx]
        # Finding missing
        missing = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i+1
        return [duplicate, missing]

        
        """ Approach3 :  Using Mathematical Equation 
            Time : O(n)
            Space : O(1)
        """
        n = len(nums)

        actual_sum = sum(nums)
        expected_sum = (n*(n+1))//2

        duplicate_minus_missing =  actual_sum - expected_sum
        print("duplicate_minus_missing",duplicate_minus_missing)

        actual_squared_sum = sum(ele*ele for ele in nums)
        expected_squared_sum = (n*(n+1)*(2*n+1))//6

        duplicate_plus_missing = (actual_squared_sum - expected_squared_sum)//duplicate_minus_missing
        print("duplicate_plus_missing",duplicate_plus_missing)

        duplicate = (duplicate_plus_missing + duplicate_minus_missing)//2
        missing = duplicate_plus_missing - duplicate

        return [duplicate,missing]


        """ Approach 4 :  XOR partioning Approach 
            Time : O(n)
            Space : O(1)
        """
        n = len(nums)
        x = 0
        # xor of all expected numbers
        for i in range(1,n+1):
            x ^= i

        # xor of nums with expected numbers
        for i in range(n):
            x ^= nums[i]
        
        # Seperating, x = duplicate xor missing
        mask = x & (-x)
        group1 = 0      # candidate1
        group2 = 0      # candidate2

        for i in range(1,n+1):
            if i & mask > 0:
                group1 ^= i
            else:
                group2 ^= i
        
        for i in range(n):
            if nums[i] & mask > 0:
                group1 ^= nums[i]
            else:
                group2 ^= nums[i]
        
        # searching both candiate in nums
        if group1 in nums:
            return [group1,group2]
        else:
            return [group2,group1]






        


        

            



        