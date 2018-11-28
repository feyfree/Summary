class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.data, end='')
			cur_node = cur_node.next


	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return 

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, pre_node, data):
		if not pre_node:
			print('Previous node is not in the list')
			return
		
		new_node = Node(data)
		new_node.next = pre_node.next
		pre_node.next = new_node

	#deletion for specific node data
	def delete_node(self, key):
		cur_node = self.head

		if cur_node and cur_node.data == key:
			self.head = cur_node.next
			cut_node = None
			return
		
		prev = None
		while cur_node and cur_node.data != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return

		prev.next = cur_node.next
		cur_node = None

	#deletion for specific node position
	def delete_node_at_pos(self, pos):
		cur_node = self.head
		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return

		prev = None
		count = 0
		while cur_node and count != pos:
			prev = cur_node
			cur_node = cur_node.next
			count += 1

		if cur_node is None:
			return 

		prev.next = cur_node.next
		cur_node = None

	# def __len__(self):
	# 	cur_node = self.head
	# 	count = 0
	# 	while cur_node:
	# 		count += 1	
	# 		cur_node = cur_node.next
	# 	return count

	def length_iter(self):
		cur_node = self.head
		count = 0
		while cur_node:
			count += 1
			cur_node = cur_node.next
		return count

	def len_recur(self, node):
		if node is None:
			return 0
		return 1 + self.len_recur(node.next)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('F')
llist.insert_after_node(llist.head.next, 'D')
llist.delete_node_at_pos(2)
# print(len(llist))
print(llist.length_iter())
print(llist.len_recur(llist.head))

llist.print_list()


