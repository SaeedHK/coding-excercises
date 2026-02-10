"""
Description: Design a hit counter that counts hits received in the past 5 minutes (300 seconds).
"""

from collections import deque


class HitCounterQueue:
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()

        return len(self.queue)


class HitCounterCircular:
    def __init__(self):
        self.times = [0] * 300  # stores the timestamp that "owns" this bucket
        self.hits = [0] * 300  # stores the count for that bucket

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300

        if self.times[idx] < timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]

        return total
