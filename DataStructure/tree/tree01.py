class Stack(object):
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def size(self):
		return len(self.items)

	def __len__(self):
		return self.size()


class Queue(object):
	def __init__(self):
		self.items = []
	#加入队列
	def enqueue(self, item):
		self.items.insert(0, item)
	#移除队列
	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()

	def is_empty(self):
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].value

	def __len__(self):
		return self.size()

	def size(self):
		return len(self.items)


class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		if traversal_type == 'pre_order':
			return self.pre_order_print(tree.root, '')
		elif traversal_type == 'in_order':
			return self.in_order_print(tree.root, '')
		elif traversal_type == 'post_order':
			return self.post_order_print(tree.root, '')
		elif traversal_type == 'level_order':
			return self.level_order_print(tree.root)
		elif traversal_type == 'reverse_level_order':
			return self.reverse_level_order_print(tree.root)
		else:
			print('Traversal type' + str(traversal_type) + 'is not supported')
			return False


	def pre_order_print(self, start, traversal):
		'''
		root->left->right
		'''
		if start:
			traversal += (str(start.value)+'-')
			traversal = self.pre_order_print(start.left, traversal)
			traversal = self.pre_order_print(start.right, traversal)
		return traversal

	def in_order_print(self, start, traversal):
		'''
		left->root->right
		'''
		if start:
			traversal = self.in_order_print(start.left, traversal)
			traversal += (str(start.value) + '-')
			traversal = self.in_order_print(start.right, traversal)
		return traversal

	def post_order_print(self, start, traversal):
		'''
		left->right->root
		'''
		if start:
			traversal = self.post_order_print(start.left, traversal)
			traversal = self.post_order_print(start.right, traversal)
			traversal += (str(start.value) + '-')
		return traversal

	def level_order_print(self, start):
		if start is None:
			return

		queue = Queue()
		queue.enqueue(start)

		traversal = ''
		while len(queue) > 0:
			traversal += str(queue.peek()) + '-'
			node = queue.dequeue()
			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		return traversal

	def reverse_level_order_print(self, start):
		if start is None:
			return
		'''
		1.设置队列，堆栈
		2.将起点压入栈
		'''

		queue = Queue()
		stack = Stack()
		queue.enqueue(start)

		traversal = ''
		while len(queue) > 0:
			node = queue.dequeue()
			stack.push(node)

			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)
		while len(stack) > 0:
			node = stack.pop()
			traversal += str(node.value)+'-'
		return traversal

	def height(self, node):
		if node is None:
			return -1
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		return 1 + max(left_height, right_height)

	#递归方法实现
	def size_(self, node):
		if node is None:
			return 0
		return 1 + self.size_(node.left) + self.size_(node.right)


	def size(self):
		if self.root is None:
			return 0

		stack = Stack()
		stack.push(self.root)
		size = 1
		while stack:
			node = stack.pop()
			if node.left:
				size += 1
				stack.push(node.left)
			if node.right:
				size += 1
				stack.push(node.right)
		return size




#.     1
#   /    \
#  2      3
# / \.   /.\
#4.  5   6. 7
#
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_tree('pre_order'))
print(tree.print_tree('in_order'))
print(tree.print_tree('post_order'))
print(tree.print_tree('level_order'))
print(tree.print_tree('reverse_level_order'))
print(tree.height(tree.root))
print(tree.size())
print(tree.size_(tree.root))  