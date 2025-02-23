class MedianFinder:
    nums = []

    def __init__(self):
        self.nums = []
        return

    def addNum(self, num: int) -> None:
        for index, val in enumerate(self.nums):
            if num < val:
                self.nums.insert(index, num)
                return
        self.nums.append(num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        return (self.nums[mid] + self.nums[mid - 1]) / 2 if len(self.nums) % 2 == 0 else self.nums[mid]

# len2 => 0 1
# len4 => 0 1 2 3
