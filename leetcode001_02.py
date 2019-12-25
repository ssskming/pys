class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]

if __name__ == "__main__":
    nums = [2,7,9,11]
    target = 18
    solu = Solution()
    print(solu.twoSum(nums,target))