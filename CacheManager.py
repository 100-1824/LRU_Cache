from LRUCache import LRUCache

class CacheManager:
    def __init__(self, cache_capacity):
        self.cache = LRUCache(cache_capacity)

    def get_data(self, key):
        # Simulate fetching data from a database or another data source
        print(f"Fetching data for key: {key}")
        return f"Data for {key}"

    def get_cached_data(self, key):
        # Check if data is in the cache
        cached_data = self.cache.get(key)
        if cached_data is not None:
            print(f"Data found in cache for key: {key}")
            return cached_data
        else:
            # Fetch data from the data source
            data = self.get_data(key)
            # Cache the fetched data
            self.cache.put(key, data)
            print(f"Data cached for key: {key}")
            return data

    def invalidate_cache(self, key):
        # Invalidate the cache entry for the specified key
        if key in self.cache.cache:
            del self.cache.cache[key]
            self.cache.order.remove(key)
            print(f"Cache entry invalidated for key: {key}")

    def print_cache_contents(self):
        self.cache.print_cache()

