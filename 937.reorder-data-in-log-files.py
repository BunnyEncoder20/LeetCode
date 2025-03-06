#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        # seperate the logs
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        # sort the letter logs
        letter_logs.sort(key=lambda log: (" ".join(log.split()[1:]), log.split()[0]))
        
        return letter_logs + digit_logs
# @lc code=end

