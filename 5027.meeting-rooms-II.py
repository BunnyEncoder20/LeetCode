from typing import List

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List) -> int:
        starttimes, endtimes = [],[]
        for st, et in intervals:
            starttimes.append(st)
            endtimes.append(et)
        
        # sort chronologically
        starttimes.sort()
        endtimes.sort()

        # start and end pointers
        spt, ept = 0, 0

        # to count max meetings rooms
        count, maxCount = 0, 0

        while st < len(starttimes):
            # case 1: new meeting started, need a room
            if starttimes[spt] < endtimes[ept]:
                count += 1
                maxCount = max(maxCount, count)
                spt += 1
            
            # case 2: meeting ended so room freed
            else:
                count -= 1
                ept += 1
        
        return maxCount

