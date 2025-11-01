class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # If no instance exists, create one
            cls._instance = super().__new__(cls)
        return cls._instance  # Always return the same instance

    def __init__(self, value):
        # __init__ will be called every time the class is instantiated,
        # but the instance itself will be the same.
        # You might want to handle re-initialization logic here if needed.
        if not hasattr(self, '_initialized'):  # Prevent re-initialization of attributes
            self.value = value
            self._initialized = True

# Example usage:
s1 = Singleton("First instance")
print(f"s1: {s1}, value: {s1.value}")

s2 = Singleton("Second instance") # This will return the same instance as s1
print(f"s2: {s2}, value: {s2.value}")

print(f"Are s1 and s2 the same object? {s1 is s2}")

s1.value = "Modified value"
print(f"s2 value after s1 modification: {s2.value}")