class Solution:
    def numberOfSteps(self, num: int) -> int:
        actions_count = 0

        while num != 0:
            actions_count = actions_count + 1
            if num % 2 == 0:
                num = num / 2
            else: num = num - 1

        return actions_count