from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_timestamp_map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        time_map = self.key_timestamp_map.get(key)
        if time_map:
            time_map[timestamp] = value
        else:
            time_map = {}
            time_map[timestamp] = value
            self.key_timestamp_map[key] = time_map
        
    def get(self, key: str, timestamp: int) -> str:
        time_map = self.key_timestamp_map.get(key)
        if time_map:
            if time_map.get(timestamp):
                return time_map[timestamp]
            else:
                latest_timestamp = timestamp - 1
                while latest_timestamp > 0:
                    if time_map.get(latest_timestamp):
                        return time_map[latest_timestamp]
                    latest_timestamp -= 1
                return ""
        else:
            return ""
        
