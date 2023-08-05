class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_lsit:
	def __init__(self):
		self.head=node()

	# Adds new note conatinig 'data' to the end of the linked lsit.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	#Returns the length (integer) of the linked list.
	def length(self):
		cur = self.head
		total = 0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total

	# Prints out the linked list in traditional Python list format.
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	# Returns the value of the node at 'index'.
	def get(self,index):
		if index>=self.length() or index<0:
			print("ERROR: 'Get' Index out of range!")
			return new_node
		cur_ind=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	def erase(self,index):
		if index>=self.length() or index<0: # added 'index<0'
			print("ERROR: 'Get' Index out of range!")
			return
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

	# Allows for bracket operator syndax (i.e. a[0] returns first item).
	def __getitem__(self,index):
		return self.et(index)

