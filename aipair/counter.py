# Create a class Counter
# Provide the following methods:
# - __init__(self, count=0): Initialize the counter with a given count (default is 0).
# - increment(self): Increment the counter by 1.
# - decrement(self): Decrement the counter by 1.
# - reset(self): Reset the counter to 0.
# - get_count(self): Return the current count.      

class Counter:
    def __init__(self, count=0):
        """Initialize the counter with a given count (default is 0)."""
        self.count = count

    def increment(self, step=1):
        """Increment the counter by 1."""
        self.count += step

    def decrement(self):
        """Decrement the counter by 1."""
        self.count -= 1

    def reset(self):
        """Reset the counter to 0."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
    

# Example usage:
if __name__ == "__main__":
    counter = Counter()
    print("Initial count:", counter.get_count())  # Output: 0
    counter.increment()
    print("After increment:", counter.get_count())  # Output: 1
    counter.decrement()
    print("After decrement:", counter.get_count())  # Output: 0
    counter.reset()
    print("After reset:", counter.get_count())  # Output: 0

