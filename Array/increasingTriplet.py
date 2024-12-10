class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


# brute force solution
# For an nums[i]
# we iterate through all nums[j] where j > i
# and check if there is a nums[k] where k > j

# o(n^3)

# sort, maintain a index array
# [2,1,5,0,4,6]
# [0,1,2,3,4,5]

# [0,1,2,4,5,6]
# [3,1,0,4,2,5]
#      ^   ^ ^
# o(nlogn)
    # num_map = {}
    # for i in range(len(nums)):
    #     num_map[nums[i]] = i
    # print(num_map)
    # sorted_map = dict(sorted(num_map.items()))
    # print(sorted_map)




# [2,1,5,0,4,6]
#    ^ ^     ^
# [2,1,5,0,4,6]
#        ^ ^ ^
# case: dont update min
# [2,1,5,0,6]
#    ^ ^   ^

# case: update min
# [7,8,5,0,4,6]
        

# [0, 100, 5, 6]

# maintain smallest number
# min = 1
# res = [1, 5]
# if larger than min, add to res
# if smaller than min, set min, clear and add to res
# min = 0
# res = [0]

# don't have to return smallest, just true or false.

# [2,1,5,0,4,6]
#        ^ ^ ^

# [1,2,7,6,5]
#  ^ ^ ^

# [1,2,10,2,9,8]
#  ^ ^  ^
# [1,10,2,9,8]
#           
# [1,3,2,4]