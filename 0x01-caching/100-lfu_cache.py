#!/usr/bin/env python3
'''
This module introduces a class
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements
    a caching system using the LFU (Least Frequently Used) algorithm.

    Attributes:
        MAX_ITEMS (int): Maximum number of items the cache can hold.
        cache_data (dict): Dictionary to store cached items.
        frequency (dict): Dictionary to store the frequency of item access.
        usage (dict): Dictionary to store the order of item access.

    Methods:
        __init__: Initializes an instance of the LFUCache class.
        put: Inserts an item into the cache or updates the existing item.
        get: Retrieves an item from the cache based on the provided key.
        print_cache: Prints the current contents of the cache.
    """

    def __init__(self):
        """
        Initializes an instance of the LFUCache class.
        """
        super().__init__()
        self.frequency = {}  # Dictionary to store frequency of item access
        self.usage = {}      # Dictionary to store order of item access

    def put(self, key, item):
        """
        Inserts an item into the cache or updates the existing item.
        If the cache is full, it applies LFU eviction to
        remove the least frequently used item.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_freq_used = [
                k for k, y in self.frequency.items() if y == min_freq
            ]

            if len(least_freq_used) > 1:
                least_recently_used = min(
                    least_freq_used, key=lambda k: self.usage.get(k, 0)
                )
                del self.cache_data[least_recently_used]
                del self.frequency[least_recently_used]
                del self.usage[least_recently_used]
                print(f"DISCARD: {least_recently_used}")

            else:
                discard_key = least_freq_used[0]
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                del self.usage[discard_key]
                print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.usage[key] = len(self.usage) + 1

    def get(self, key):
        """
        Retrieves an item from the cache based on the provided key.
        If the key doesn't exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage[key] = len(self.usage) + 1

        return self.cache_data[key]
