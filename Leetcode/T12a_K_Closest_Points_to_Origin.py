# _source_ https://leetcode.com/problems/k-closest-points-to-origin/
# _Topic_ @2 Pattern: Top K Numbers
# _Name_ 973. K Closest Points to Origin
# _Q_ @12. a)
# _Difficulty_ medium
# Time taken until for own solution, without compiling the code: 25min, incorrect
# Time to solve (total): 80min

# Problem Statement:
"""
"""

# My solution
# first try: 25min (without compile)
# first try: 35min total (with compile)
# second try: 20min with compile.
import math
import heapq

class Solution:
    def calc_distance(self, xy_coord: List[int]):
        return math.sqrt(xy_coord[0] ** 2 + xy_coord[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use heap
        max_heap = []
        final_list = []

        for i in range(k):
            heappush(max_heap, (-1 * self.calc_distance(points[i]), points[i]))
            final_list.append(points[i])

        for i in range(k, len(points)):
            # don't forget about distance.
            if -1 * self.calc_distance(points[i]) > max_heap[0][0]:
                final_list.remove(heappop(max_heap)[1])

                heappush(max_heap, (-1 * self.calc_distance(points[i]), points[i]))
                final_list.append(points[i])

        return final_list

""" Asymptotics:
For sols: 
Time: O(n*log(n))
Space: O(n)
For mine: 
Time: O(n*log(n)), but slow, only beats 5% apparently
Space: O(n) (2n), others use n only. Still O(n).
"""

## ANSWER:
# really good except the unnecessary Haskell-isation...
# takeaway point is use the heap simply.
class Sol_Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, self._distance(p))
        return [heapq.heappop(heap)[1:] for i in range(k)]

    def _distance(self, p: List[int]) -> float:
        return [self._get_euclidean_distance(p, [0,0]), *p]

    def _get_euclidean_distance(self, p: List[int], q: List[int]) -> float:
        return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


# lol
class Sol_Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
# not even using heap, but I gues sorting is also O(nlog(n)) so oh well.
