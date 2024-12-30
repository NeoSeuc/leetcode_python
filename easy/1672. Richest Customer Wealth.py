from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])

        return max(accounts)


solution = Solution()

accounts = [[1, 2, 3], [3, 2, 1]]
assert solution.maximumWealth(accounts) == 6
