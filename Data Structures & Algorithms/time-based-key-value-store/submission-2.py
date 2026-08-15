class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.kv:
            return ""
        else:
            l, r = 0, len(self.kv[key]) - 1
            while l <= r:
                mid = (l + r)//2
                if self.kv[key][mid][0] == timestamp:
                    return self.kv[key][mid][1]
                elif self.kv[key][mid][0] > timestamp:
                    r = mid - 1
                else:
                    res = self.kv[key][mid][1]
                    l = mid + 1
        return res

