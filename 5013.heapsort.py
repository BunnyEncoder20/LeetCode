class Solution:
    def heapSort(self, nums):
        # func to max heap nums
        self.buildMaxHeap(nums)

        # last index
        last = len(nums)-1

        # until there are elements on left
        # to sort in the array
        while last > 0:
            # swap the maxheap top and last index
            nums[0], nums[last] = nums[last],nums[0]
            last -= 1   # shrink unsorted part

            if last > 0:
                # heapify down the root
                self.heapifyDown(nums, last, 0)
        return 
    
    def buildMaxHeap(self, nums):
        n = len(nums)
        for i in range(n//2 - 1, -1, -1):
            self.heapifyDown(nums, n-1, i)
        return 

    def heapifyDown(self, nums, last, idx):
        # init idxes 
        largestIdx = idx
        leftChildIdx = 2 * idx + 1
        rightChildIdx = 2 * idx + 2

        # find with child of larger value
        if leftChildIdx <= last and nums[leftChildIdx] > nums[largestIdx]:
            largestIdx = leftChildIdx
        if rightChildIdx <= last and nums[rightChildIdx] > nums[largestIdx]:
            largestIdx = rightChildIdx
        
        # if largestIdx updated
        if largestIdx != idx:
            # swap with largest child node
            nums[largestIdx], nums[idx] = nums[idx],nums[largestIdx]

            # recursively heapify the lower subtree
            self.heapifyDown(nums, last, largestIdx)
        return