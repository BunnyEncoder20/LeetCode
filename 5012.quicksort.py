class Solution:
    def quickSort(self, nums):
        self.divider(nums, 0, len(nums)-1)
        return nums
    
    def divider(self, nums, low, high):
        if low < high:
            partitionIdx = self.placePivot(nums, low, high)
            self.divider(nums, low, partitionIdx-1)
            self.divider(nums, partitionIdx+1, high)
    
    def placePivot(self, nums, low, high):
        pivot = nums[low]
        i = low
        j = high

        while i < j:
            while nums[i] <= pivot and i <= high-1: i += 1
            while nums[j] > pivot and j >= low+1: j -= 1
            if i < j: nums[i],nums[j] = nums[j],nums[i]

        # place pivot at j and return j 
        nums[low],nums[j] = nums[j], nums[low]
        return j
