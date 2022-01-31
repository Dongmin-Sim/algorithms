import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        answer = []

        for _ in range(k):
            answer.append(heapq.heappop(freqs_heap)[1])
        
        return answer


    def topKFrequent_pythonic(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]