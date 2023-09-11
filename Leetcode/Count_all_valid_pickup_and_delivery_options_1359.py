# Link: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
# Date: 11-09-2023
# Brief: Given n orders, each order consist in pickup and delivery services.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).
# Since the answer may be too large, return it modulo 10^9 + 7.
# Input: n = 1
# Output: 1
# Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

# Constraints:
# 1 <= n <= 500

class Solution:
    def countOrders(self, n: int) -> int:
        output = {}
        output[1] = 1
        for d in range(2, n+1):
            output[d] = (output[d-1]*(2*d-1)*d) % int(1e9 + 7)
        return output[n]