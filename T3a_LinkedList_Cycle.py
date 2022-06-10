# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/3.%20Pattern%20Fast%20%26%20Slow%20pointers/LinkedList%20Cycle%20(easy).py
# _Topic_ @3 Pattern: Fast & Slow pointers
# _Q_ @3. a)
# _Difficulty_ easy

# Problem Statement:
"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

# My solution:
# if the slow pointer ends up in front of fast pointer, then 
class Node:
	def __init__(self, value, next=None):
		self.val = value
		self.next = next

def has_cycle(head):
	tortoise = head
	rabbit = head
	while rabbit.next.next != None or rabbit.next == None:
		if rabbit.next == tortoise:
			return True
		tortoise = tortoise.next
		rabbit = rabbit.next.next
	return False
