# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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