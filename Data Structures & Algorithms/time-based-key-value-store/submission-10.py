class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []

        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        values = self.keys[key]

        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result 