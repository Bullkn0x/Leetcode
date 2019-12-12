'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) < 2:
            return 0
        
        
        prev_cost = [0] * len(cost)
        # The cost to get to stair index zero and stair index one is just the stair's cost
        prev_cost[:2] = cost[:2] 
        i = 2
        while i < len(cost):
            # Min cost to get to stair i is equal to stair i + min of the values of the two previous stairs
            prev_cost[i] = cost[i] + min(prev_cost[i-2:i])
            i += 1
        
        return min(prev_cost[-2:])
        