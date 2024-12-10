class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # Pick 2 numbers from nums
        # If 2 numbers equal to k, remove
        # Return number of operations
        #  7 3.5 8 4

        # Does order matter? No. 
        # nums = [1, 2, 4, 2], k = 5

        # [1,2,3,4] k = 5
        #    ^ ^
        # [1,2] 
        #  ^ ^

        # [7,1,3,5,7,2,1] k = 8
        # [1,1,2,3,5,7,7] sum = 8, remove
        #        ^ ^
        # [1,1,2,7,7] sum = 9 > k, shift left pointer
        #      ^ ^
        #    ^   ^ sum = 8, remove
        # [1,2,7]
        #    ^ ^
        #  ^   ^

        # [1,2,4,3,1,2,3] k = 6
        # [1,1,2,2,3,3,4] sum = 5 < k, shift right pointer 
        #        ^ ^
        #        ^   ^
        #        ^     ^ sum = 6, remove
        #  [1,1,2,3,3]
        #       ^ ^
        #       ^   ^ Exit.

        # [3,3,3,3,3] k = 2
        #      ^ ^
        #    ^   ^
        #  ^     ^ Exit.

        # [5,5,5,5,5] k = 13
        #      ^ ^
        #      ^   ^ Exit.

        # operations_count = 0
        # high = round(len(nums) / 2) 
        # low = high - 1
        # nums.sort()

        # First iteration failed since left and right not seen
        # while low > 0 and high < len(nums):
        #     if nums[low] + nums[high] == k:
        #         operations_count += 1
        #         nums.pop(low) 
        #         nums.pop(high)
        #         high = round(len(nums) / 2) 
        #         low = high - 1
        #     elif nums[low] + nums[high] > k: 
        #         # sum > k, shift low 
        #         low -= 1
        #     else:
        #         # sum < k, shift high  
        #         high += 1
        # return operations_count



        # [1,2,4,3,1,2,3] k = 2
        # [1,1,2,2,3,3,4]
        #  ^ ^

        # [1,2,4,3,1,2,3] k = 6
        # [1,1,2,2,3,3,4] sum = 5 < k, shift left pointer 
        #  ^           ^
        #    ^         ^
        #      ^       ^ sum = 6, remove
        #  [1,1,2,3,3]
        #   ^       ^
        #     ^     ^ 
        #       ^   ^ 
        #         ^ ^ 
        #  [1,1,2] Early exit? since nums[high] < k/2
        #   ^   ^
        #     ^ ^
        #       ^ Exit.
         
        # Iteration 2, failed due to taking too long
        # low = 0
        # high = len(nums) - 1
        # nums.sort()
        # operations_count = 0
        # while (low < high):
        #     if nums[low] + nums[high] == k:
        #         operations_count += 1
        #         nums.pop(high)
        #         nums.pop(low) 
        #         high = len(nums) - 1
        #         low = 0
        #     elif nums[low] + nums[high] > k: 
        #         # sum > k, shift high
        #         high -= 1
        #     else:
        #         # sum < k, shift low  
        #         low += 1
        # return operations_count

        # No sort, iterate through and hashmap. fail due to duplicates
        # [3,1,3,4,3] k = 6
        #          ^
        #  {5: 1}  1

        # [1,2,4,3,1,2,3] k = 6
        #          ^ 
        #  {5: 1, 3: 3}
            
        # [1,2,4,3,1,2,3] k = 6
        # [1,1,2,2,3,3,4]
        #  ^           ^
        #    ^         ^
        #      ^       ^
        # [1,1,2,3,3]
        #      ^   ^

        # [1,2,4,3,1,2,3] k = 5
        # [1,1,2,2,3,3,4]
        #  ^           ^
        # [1,2,2,3,3]
        #  ^       ^
        #    ^     ^, low = 1, high = 5
        # [1,2,3] 
        #    ^ ^, low = 1, high = 3
        low = 0
        high = len(nums) - 1
        nums.sort()
        operations_count = 0
        while (low < high): 
            if nums[high] < k/2: break
            if nums[low] + nums[high] == k:
                operations_count += 1
                nums.pop(high)
                nums.pop(low) 
                high -= 2
            elif nums[low] + nums[high] > k: 
                # sum > k, shift high
                high -= 1
            else:
                # sum < k, shift low  
                low += 1
        return operations_count 
