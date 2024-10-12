import time

counts = [1000, 1000, 10000, 100000, 1000000]

for count in counts:
    print(f"Testing with count = {count}")

    # Create a large bytearray and modify it in-place (efficient)
    def optimized_bytearray():
        data = bytearray(count)  # Pre-allocate 1 million bytes
        for i in range(len(data)):
         data[i] = i % 256  # Modify in place
        return data
    # Create new bytes objects repeatedly (inefficient)
    def inefficient_bytes():
        data = bytes()  # Start with empty bytes
        for i in range(count):
            data += bytes([i % 256])  # Create new bytes object each time (inefficient)
        return data

    # Measure time for optimized bytearray
    start_time = time.time()
    optimized_bytearray()
    end_time = time.time()
    print(f"Optimized bytearray took: {(end_time - start_time)*1000:.6f} milliseconds")

    # Measure time for inefficient bytes approach
    start_time = time.time()
    inefficient_bytes()
    end_time = time.time()
    print(f"Inefficient bytearray took: {(end_time - start_time)*1000:.6f} milliseconds")
    print('-' * 40)

