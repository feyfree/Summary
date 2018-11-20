'''
希尔排序的实质是跨步逐渐插入排序
1---4----6----2----3
一开始步长为2
则从index = 2 开始， 
对6判断，不出现交换
对2判断， 和4比，交换1----2---6----4---3
对3判断1----2-----3-----4-----6
完成
'''

def shell_sort(nums):
	step = len(nums)//2
	while step > 0:
		for i in range(step, len(nums)):
			while i >= step and nums[i-step] > nums[i]:
				nums[i], nums[i-step] = nums[i-step], nums[i]
				i -= step
		step = step // 2
	return nums

nums = [1,4,6,2,3]
print(shell_sort(nums))