from CacheManager import CacheManager

if __name__ == "__main__":
    # Create a Cache Manager with a capacity of 3
    cache_manager = CacheManager(cache_capacity=3)

    # Fetch and cache data for keys
    cache_manager.get_cached_data("user1")
    cache_manager.get_cached_data("user2")
    cache_manager.get_cached_data("user3")

    # Print cache contents
    cache_manager.print_cache_contents()

    # Fetch data for a new key (user4)
    cache_manager.get_cached_data("user4")

    # Print updated cache contents
    cache_manager.print_cache_contents()

    # Invalidate the cache for user2
    cache_manager.invalidate_cache("user2")

    # Print cache contents after invalidation
    cache_manager.print_cache_contents()

