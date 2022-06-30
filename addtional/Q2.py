'''
Problem Statement 
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
If the total number of nodes in the LinkedList is even, return the second middle node.
Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3
Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	# from answers:
	def print_list(self):
		temp = self
		while temp is not None:
			print(temp.value, end=" ")
			temp = temp.next
		print()

## fast & slow pointers
def find_middle_of_LL(head):  # takes head of LL
	if head is None:
		return None

	slow, fast = head, head
	while fast is not None and fast.next is not None:  ## OR!!!
		fast = fast.next.next
		slow = slow.next
	# even odd distinction
	if fast is None:
		return slow.next
	else:
		return slow # return pointer to middle node

def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.print_list()
	answer = find_middle_of_LL(head)
	print("the middle of the list is:", answer.value)

main()
