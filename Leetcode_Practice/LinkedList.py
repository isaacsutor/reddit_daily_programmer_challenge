# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MiddleOfTheLinkedList876:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3:25 Time
        # 32 ms | 69%
        # 14.2MB  | 43%
        front_runner = head
        back_runner = head
        while(front_runner.next != None and front_runner.next.next != None):
            front_runner = front_runner.next.next
            back_runner = back_runner.next
            
        if(front_runner.next != None):
            return back_runner.next
        return back_runner







class ConvertBinaryNumberInLinkedListToInteger1290:
    def getDecimalValue(self, head: ListNode) -> int:
        # Brute Force 11:45 Time
        # 52 ms | 10%
        # 32MB  | 37.5%
        current = head
        counter = 0
        decimalValue = 0
        while(current.next != None):
            current = current.next
            counter += 1
        current = head
        while(counter >= 0):
            if(current.val == 1):
                decimalValue += 2 ** counter
            current = current.next
            counter -= 1
            
        return decimalValue