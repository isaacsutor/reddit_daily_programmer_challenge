class RichestCustomerWealth1672:
    # Time: 4:16
    def maximumWealthRefined(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for customer in accounts:
            wealth = sum(customer)
            maxWealth = max([wealth, maxWealth])
        return maxWealth
    # Time: 2:48
    def maximumWealthBrute(self, accounts: List[List[int]]) -> int:
        wealths = []
        for customer in accounts:
            wealth = 0
            for bank in customer:
                wealth += bank
            wealths.append(wealth)
        return max(wealths)

class FinalValueOfVariableAfterOperations2011:
    # Time: 3:32
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if(op == 'X++' or op == '++X'):
                x+=1
            elif(op == 'X--' or op == '--X'):
                x-=1
        return x


class ConcatenationOfArray1929:
    # Time: 6:30 
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums)*2)
        for x in range(0, len(nums)):
            ans[x] = nums[x]
            ans[(x+len(nums))] = nums[x]
        return ans


class BuildArrayFromPermutation1920:
    # Time: 10:00 
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for x in range(0, len(nums)):
            ans[x] = nums[nums[x]]
        return ans