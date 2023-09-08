from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start,residue_fuel,n=0,0,len(gas)
        for i in range(n):
            if residue_fuel+gas[i]<cost[i]:
                start=(i+1)%n
                residue_fuel=0
            else:
                residue_fuel += gas[i]-cost[i]
        return start
    
sol=Solution()
gas=[1,2,3,4,5]
cost = [3,4,5,1,2]

print(sol.canCompleteCircuit(gas,cost))