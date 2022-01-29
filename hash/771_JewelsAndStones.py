from cgitb import strong
import collections 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        freqs = {}


        for s in stones:
            if s not in freqs:
                freqs[s] = 1
            else:
                freqs[s] += 1
        
        for j in jewels:
            if j in freqs:
                count += freqs[j]
        
        return count 


    def numJewelsInStonesDefaultdict(self, jewels: str, stones: str) -> int:
        count = 0
        freqs = collections.defaultdict(int)
        
        for s in stones:
            freqs[s] += 1
            
        for j in jewels:
            count += freqs[j]
            
            
        return count


    def numJewelsInStonesCounter(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0 
        
        for j in jewels:
            count += freqs[j]
            
        return count


    def numJewelsInStonesPythonic(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)