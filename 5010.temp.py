class Solution:
    def mergeSort(self, nums):
        n = len(nums)
        self.divider(nums, 0, n-1)
        return nums
    
    def divider(self, nums, low, high):
        # base case 
        if low >= high: return

        # find mid and divide
        mid = (low+high)//2
        self.divider(nums, low, mid)
        self.divider(nums, mid+1, high)

        # merge halfs
        self.merger(nums, low, mid, high)

    def merger(self, nums, low, mid, high):
        temp = []
        left = low 
        right = mid+1

        while left <= mid and right<=high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high+1):
            nums[i] = temp[i-low]
