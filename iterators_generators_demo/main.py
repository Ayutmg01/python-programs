# Example of a basic Iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
print("Iterator Example:")
data = [1, 2, 3, 4, 5]
iterator = MyIterator(data)
for item in iterator:
    print(item)

print("\n")

# Example of a basic Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Generator Example:")
for num in countdown(5):
    print(num)

print("\n")

# Generator for Fibonacci sequence
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Fibonacci Generator:")
for num in fibonacci(10):
    print(num)

print("\n")

# Memory-efficient generator: Reading lines from a large file
def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

# Test the file reading generator
print("File Reading Generator:")
for line in read_file_line_by_line('iterators_generators_demo/example.txt'):
    print(line)

