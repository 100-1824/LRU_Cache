class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Evict the least recently used entry
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

        # Add the new entry to the cache and the end of the order list
        self.cache[key] = value
        self.order.append(key)

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache.items():
            print(f"{key}: {value}")
        print("---")

