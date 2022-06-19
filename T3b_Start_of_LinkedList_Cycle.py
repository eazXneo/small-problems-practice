# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/3.%20Pattern%20Fast%20%26%20Slow%20pointers/Start%20of%20LinkedList%20Cycle%20(medium).py
# _Topic_ @3 Pattern: Fast & Slow pointers
# _Q_ @3. b)
# _Difficulty_ medium

# Problem statement:
"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""
# NOTES: TAKE CARE WHEN RETURNING NODE / VALUE DIRECTLY !?!

# from answer
from __future__ import print_function  # should be fine since it's not used higher up.
# My solution:
# looks hard :(
class MY_Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

def MY_find_cycle_start(head):
    # use previous solution
    # then take only slow and new pointer
    # check where they meet, new pointer counts;
    # that's the position.
    slow, fast = head, head
    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            # found a cycle
            find_cycle = head  # new pointer
            position = 1  # counter for position of cycle start
            while find_cycle != slow:
                find_cycle = find_cycle.next
                slow = slow.next
                position += 1
            return position
    return -1  # no cycle found

## ANSWER

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self  # did we need the variable? Why not just 'self.next'
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()

def find_cycle_start(head):
    cycle_length = 0
    # find the LinkedList cycle
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):  # is this necessary for this question??
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

""" Asymptotics:
For sols: O(3n) = O(n)
For mine: O(2n)... 
    something is not quite right... 
Space complexity: O(1) -> original LL + pointers.
"""

## ALT ANSWER
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def detectCycle(head: Node) -> Node:
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            current = head
            while current is not slow:
                current = current.next
                slow = slow.next
            return slow.value
    return None


# Additional code.
# BEWARE: Starts index at 1!
def main():
    print("My answer:")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(MY_find_cycle_start(head)))
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(MY_find_cycle_start(head)))
    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(MY_find_cycle_start(head)))

    print("Solutions:")
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    print("Alternative solution:")
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(detectCycle(head)))
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(detectCycle(head)))
    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(detectCycle(head)))
main()
