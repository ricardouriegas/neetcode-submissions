class TimeMap:

    def __init__(self):
        self.array = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.array:
            self.array[key] = []

        self.array[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.array:
            return ""

        values = self.array[key]

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