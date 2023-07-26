#
# @lc app=leetcode id=1870 lang=python3
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour : return -1
        if len(dist) == 1: return int(dist[-1]/hour) if int(dist[-1]/hour) * hour >= dist[-1] else int(dist[-1]/hour) + 1
        last = dist.pop()
        dist.sort()
        max_v = max(int(last / (hour - len(dist))) + 1, dist[-1], last)
        min_v = min(dist[0], int((sum(dist)+last)//hour))
        if min_v == 0: min_v += 1
        def time_v(dist, v, last):
            time = 0
            for i in range(-1,-len(dist)-1, -1):
                if dist[i] / v > 1:
                    time += dist[i] // v
                    if dist[i] % v != 0: time +=1
                else:
                    time += i + len(dist) + 1
                    break
            time += last / v 
            return time
        while min_v <= max_v:
            mid_v = (min_v + max_v) // 2
            if time_v(dist, mid_v, last) <= hour:
                if time_v(dist, mid_v + 1, last) > hour: return mid_v
                else: max_v = mid_v - 1
            elif time_v(dist, mid_v, last) > hour:
                if time_v(dist, mid_v + 1, last) < hour: return mid_v + 1
                else: min_v = mid_v + 1
        return min_v 
                 
# @lc code=end

