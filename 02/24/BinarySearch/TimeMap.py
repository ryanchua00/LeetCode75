class TimeMap:

    def __init__(self):
        # hashmap of string - [(string, int)]
        self.timemap = {}

    # strictly increasing timestamp order

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            node = self.timemap[key]
            node.append((value, timestamp))
        else:
            node = [(value, timestamp)]
            self.timemap[key] = node

    def get(self, key: str, timestamp: int) -> str:
        # most recent value of key
        # IF set has been called on it -- key exists
        # AND timestamp of entry <= given timestamp
        # if no values return ""
        if key not in self.timemap:
            return ""
        node = self.timemap[key]
        left, right = 0, len(node)

        while left <= right:
            mid = left + (right - left) // 2
            if node[mid][1] > timestamp:
                right = mid - 1
            elif node[mid][1] < timestamp:
                left = mid + 1
            else:
                return node[mid][0]

        return node[left][0] if node[left][1] <= timestamp else ""
