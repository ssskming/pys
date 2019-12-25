
nums = [2,7,9,11]
target = 9
#def twoSum(nums,target):
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0,len(nums)):
                for j in range(0,len(nums)):
                    if (nums[i]+nums[j]==target):
                        return [i,j]

print (twoSum(nums,target))