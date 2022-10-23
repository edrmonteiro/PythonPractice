class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] >= target:
                end = mid-1
            else:
                start = mid+1
        return -1

solution= Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(solution.search(nums, target))

