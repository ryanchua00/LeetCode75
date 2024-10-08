class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isSorted = False
        while not isSorted:
            isSorted = True
            index = 0
            while(index < len(nums) - 1):
                if nums[index] > nums[index + 1]:
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
                    isSorted = False
                index += 1