from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

# Function reverse a linked list
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # # Solution 1: using list to store all node value
    # # Time complexity: O(n)
    # # Space complexity: O(n)
    # reversed_nodes = []
    # current = head
    # while current is not None:
    #     reversed_nodes.append(current.val)
    #     current = current.next
    # # reset current node
    # current = head
    # # update nodes' value
    # for val in reversed_nodes[::-1]:
    #     current.val = val
    #     current = current.next
    # return head

    # Solution 2: not using extra space, using 2 pointer
    # Time complexity 
    prev = None
    current = head
    # 1->2->3->4->5->None
    # None<-1
    # while current is not None
    while current:
        # store next node of current
        next_temp = current.next
        # re-assign next node of current is prev
        current.next = prev
        # re-assign prev node to current
        prev = current
        # re-assign current node to next_temp
        current = next_temp
    # after last move, current =  None, prev is the last node. So, return prev
    return prev 

# Return True if detect Cycle
# Return False if detect no Cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # check edge case when head is None, no Cycle
    if head is None: 
        return False
    # Solution 1: Using a  set of seen_nodes
    seen_nodes = set()
    current = head
    while current:
        if current in seen_nodes:
            return True
        # add current to seen_nodes
        seen_nodes.add(current)
        # move current 1 step
        current = current.next
    return False

# Function set up linked list
def setup_linkedlist(values):
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    head = dummy.next
    return head

# Function check reverse linked list
def run_reverseList():
    values = [1, 2, 3, 4, 5]
    # Reverse the list
    reversed_head = reverseList(None, setup_linkedlist(values))  # Pass None for self

    # Print reversed list
    curr = reversed_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

def checkCycle():
    # Create nodes
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)

    # Link nodes
    head.next = second
    second.next = third
    third.next = fourth

    # Create a cycle: 4 -> 2
    fourth.next = second
    print(f"{hasCycle(None, head)}")


def main():
    run_reverseList()
    checkCycle()

if __name__ == "__main__":
    main()
