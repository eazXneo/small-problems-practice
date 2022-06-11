# _source_ https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/3.%20Pattern%20Fast%20%26%20Slow%20pointers/LinkedList%20Cycle%20(easy).py
# _Topic_ @3 Pattern: Fast & Slow pointers
# _Q_ @3. a)
# _Difficulty_ easy

# Problem Statement:
"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

# My solution:
# if the slow pointer ends up in front of fast pointer, then
class MY_Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def MY_has_cycle(head):
    tortoise = head
    rabbit = head
    while rabbit.next.next != None or rabbit.next != None:
        # does the order of parts matter?? It does because otherwise it exits at start!!!!
        # part B
        tortoise = tortoise.next
        rabbit = rabbit.next.next
        # part A
        if rabbit.next == tortoise:
            return True
    return False

## ANSWER
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

""" Asymptotics:
For sols (mine): O(n) 
    -> slow tortoise will be caught up with at max end of list
Space complexity: O(1), no extra space needed (except pointers, so constant)
"""


# Additional code.
