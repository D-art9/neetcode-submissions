class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        size = n + 1
        minc = [0] * size
        minc[0] = 0
        minc[1] = 0
        for i in range(2, size):
            minc[i] = min(minc[i-1] + cost[i-1], minc[i-2] + cost[i-2])
        return minc[n]

        