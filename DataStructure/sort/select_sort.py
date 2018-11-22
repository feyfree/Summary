def select_sort(nums):
	n = len(nums)
	for i in range(n):
		k = i 
		for j in range(i, n):
			if nums[j] < nums[k]:
				k = j
		if i != k:
			nums[i], nums[k] = nums[k], nums[i]
	return nums

nums = [1,3,6,7,2,4]
print(select_sort(nums))