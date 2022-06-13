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
    tortoise, rabbit = head, head
    # this line is more complicated than previously thought
    while rabbit is not None and rabbit.next is not None:
        # does the order of parts matter?? It does because otherwise it exits at start!!!!
        # part B
        tortoise = tortoise.next
        rabbit = rabbit.next.next
        # part A
        if rabbit == tortoise:
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
def main():
    print("My answer:")
    MY_head = MY_Node(1)
    MY_head.next = MY_Node(2)
    MY_head.next.next = MY_Node(3)
    MY_head.next.next.next = MY_Node(4)
    MY_head.next.next.next.next = MY_Node(5)
    MY_head.next.next.next.next.next = MY_Node(6)
    # no cycle in LL Node(6).next == None
    print("LinkedList has cycle: " + str(MY_has_cycle(MY_head)))
    MY_head.next.next.next.next.next.next = MY_head.next.next  # making node 6 point to node 3
    print("LinkedList has cycle: " + str(MY_has_cycle(MY_head)))
    MY_head.next.next.next.next.next.next = MY_head.next.next.next
    print("LinkedList has cycle: " + str(MY_has_cycle(MY_head)))

    print("Solutions:")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    # no cycle in LL Node(6).next == None
    print("LinkedList has cycle: " + str(has_cycle(head)))
    head.next.next.next.next.next.next = head.next.next  # making node 6 point to node 3
    print("LinkedList has cycle: " + str(has_cycle(head)))
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()

"""
Similar Problems 
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

# My attempt for problem 1
def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            return calculate_cycle_length(slow)
    return 0

def MY_calculate_cycle_length(slow):
    cycle_pointer = slow.next
    counter = 1
    while cycle_pointer != slow:
        cycle_pointer = cycle_pointer.next
        counter += 1
    return counter

"""
Solution: We can use the above solution to find the cycle in the LinkedList. 
Once the fast and slow pointers meet, we can save the slow pointer and 
iterate the whole cycle with another pointer until we see the slow pointer again 
to find the length of the cycle.
Here is what our algorithm will look like:
"""

def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

def main2():
    print("main2()")
    # to use MY_calculate_cycle_length(), change find_cycle_length().
    # my answer seems to give same sols as sols, however,
    # cycle just last node pointing to itself with cycle length 0(?),
    # then mine fails I think.
    print("Solutions:")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

main2()

""" Similar problem 1:
Time complexity: O(n) -> because the cycle cannot be greater than total
    length of the LL
Space complexity: O(1) -> only pointers needed
"""
