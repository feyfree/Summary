def bubble_sort(nums):
	n = len(nums)
	for i in range(n):
		flag = False       #设置判断标示符
		for j in range(1, n-i):
			if nums[j-1] > nums[j]:
				nums[j-1], nums[j] = nums[j], nums[j-1]
				flag = True   # 出现交换，标示符变为True
		if not flag:  #如果二级循环后flag还是false，则表示不执行交换条件，说明是顺序排列
			break
	return nums

nums = [1,6,8,3,4]
print(bubble_sort(nums))