
class JewelsandStones771:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Time: 1:04
        count = 0
        for x in stones:
            if(x in jewels):
                count += 1
        return count



class DefanginganIPAddress1108:
    def defangIPaddr(self, address: str) -> str:
        # Time: 2:12
        defanged = ""
        for x in address:
            if(x == "."):
                defanged += '[.]'
            else:
                defanged += x
        return defanged