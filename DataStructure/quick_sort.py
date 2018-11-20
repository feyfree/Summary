def quick_sort(nums):
	def q_sort(nums, start, end):
		if start >= end:
			return 
		pivot = nums[start]    #设置参考值，可以认为是第一个
		i = start 			   #设置参考值为第一个
		for j in range(start+1, end+1):
			if nums[j] < pivot:   # 如果在判断值的后面发现比pivot小，则在start后面的值和它交换
				i += 1
				nums[i], nums[j] = nums[j], nums[i]
		nums[start], nums[i] = nums[i], nums[start]
		q_sort(nums, start, i-1)
		q_sort(nums, i+1, end)
	q_sort(nums, 0, len(nums)-1)

nums = [1,2,6,3,4]
quick_sort(nums)
print(nums)