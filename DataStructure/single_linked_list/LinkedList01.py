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

	def print_helper(self, node, name):
		if node is None:
			print(name + ": None")
		else:
			print(name + ":" + node.data)


	def reverse_iter(self):
		'''
		iterative way:
		1.store the next node
		2.current's next node become the previous one
		3.previous becomes the current one
		4.current one become the next
		A->B->C->None
		A<-B<-C<-None
		'''
		prev = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			# self.print_helper(nxt, "NEXT")
			# self.print_helper(prev, "PREV")
			# self.print_helper(cur, "CUR")
		self.head = prev

	def reverse_recur(self):

		def _reverse_recur(cur, prev):
			if not cur:
				return prev
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return _reverse_recur(cur, prev)

		self.head = _reverse_recur(cur=self.head, prev=None)

	def merge_sorted(self, llist):
		'''
		1.judge whether the linkList is None
		2.double pointer and a seperate pointer
		3.generate new head
		4.a seperate pointer and the double pinter start moving
		'''
		p = self.head
		q = llist.head
		s = None

		if not p:
			return q
		if not q:
			return p
		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s
		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = q.next
		if not p:
			s.next = q
		if not q:
			s.next = p
		return new_head

	def remove_duplicates(self):
		'''
		1.define the previous one 
		2.while cur still exists, if cur.data not in dict,
			key = data , value=1, prev = cur, else prev.next = cur.next,

		'''
		cur = self.head
		prev = None

		temp = dict()
		while cur:
			if cur.data in temp:
				prev.next = cur.next
				# cur = None
			else:
				temp[cur.data] = 1
				prev = cur
			cur = prev.next

	def print_nth_from_last(self, n):
		total_len = self.length_iter()
		cur = self.head
		while cur:
			if total_len == n:
				print(cur.data)
				total_len -= 1
				cur = cur.next
		if cur is None:
			return 

	def rotate(self, k):
		p = self.head
		q = self.head
		prev = None
		count = 0
		while p and count < k:
			prev = p 
			p = p.next
			q = q.next
			count += 1
		p = prev

		while q:
			prev = q
			q = q.next
		q = prev

		q.next = self.head
		self.head = p.next
		p.next = None



# llist = LinkedList()
# llist.append('A')
# llist.append('B')
# llist.append('C')
# llist.append('F')
# llist.insert_after_node(llist.head.next, 'D')
# llist.delete_node_at_pos(2)
# # print(len(llist))
# print(llist.length_iter())
# print(llist.len_recur(llist.head))

# llist.print_list()
# llist.reverse_iter()
# llist.reverse_recur()
# llist.print_list()
llist1 = LinkedList()
llist2 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)
llist1.append(1)
llist1.append(8)
llist1.append(9)
llist2.append(1)
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(5)
llist2.append(6)
llist2.append(7)
# llist1.merge_sorted(llist2)
# llist1.remove_duplicates()
# llist1.print_list()
# llist1.print_nth_from_last(7)
llist1.print_list()
print('\n')
llist1.rotate(2)
llist1.print_list()





