def insert_sort(nums):
	n = len(nums)
	for i in range(n):
		for j in range(i, 0, -1):
			if nums[j] < nums[j-1]:
				nums[j], nums[j-1] = nums[j-1], nums[j]
	return nums

nums = [1,6,8,9,3,4,7]
print(insert_sort(nums))