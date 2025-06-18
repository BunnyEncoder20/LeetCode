#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            # case 1: +ve →
            if n > 0:
                stack.append(n)

            # case 2: -ve ←
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(n):
                    stack.pop()

                # case 3: equal
                if stack and stack[-1] == abs(n):
                    stack.pop()

                # case 4: empty stack && -ve only
                elif not stack or stack[-1] < 0:
                    stack.append(n)
            
        return stack
# @lc code=end

