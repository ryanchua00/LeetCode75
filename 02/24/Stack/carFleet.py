from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair position and speed, and sort according to position
        time = [0] * len(position)
        pos_spd = []
        for i in range(len(position)):
            pos_spd.append((position[i], speed[i]))

        pos_spd.sort()
        for i in range(len(pos_spd)):
            time[i] = (target - pos_spd[i][0]) / pos_spd[i][1]
        print(pos_spd)
        print(time)

        fleets = 0
        while len(pos_spd) > 0:
            curr = pos_spd.pop()
            time_taken = time.pop()
            print(time, time_taken)
            if len(pos_spd) > 0 and len(time) > 0:
                while time_taken >= time[-1]:
                    pos_spd.pop()
                    time.pop()
            fleets += 1

        return fleets


target = 12

position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

time = [1, 1, 12, 7, 4]

s = Solution()
print(s.carFleet(target, position, speed))
