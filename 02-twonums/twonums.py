from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry==0:
            return None
        if l1 is None:
            l1,l2 = l2,l1 
        s = carry + l1.val + (l2.val if l2 is not None else 0)
        l1.val = s%10
        l1.next = self.addTwoNumbers(l1.next,l2.next if l2 is not None else None,s//10)
        return l1

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    # 创建测试用例
    l1_arr = [2, 4, 3]  # 代表数字 342
    l2_arr = [5, 6, 4]  # 代表数字 465
    
    l1 = create_linked_list(l1_arr)
    l2 = create_linked_list(l2_arr)
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    print("输入链表 1:", end=" ")
    print_linked_list(create_linked_list(l1_arr))
    print("输入链表 2:", end=" ")
    print_linked_list(create_linked_list(l2_arr))
    print("结果链表:", end=" ")
    print_linked_list(result)

