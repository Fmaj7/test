# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

'''
Explanation
Using a mutable default argument like a list can lead to unexpected behavior. 
If the function is called multiple times without providing a new list, it will keep appending to the same list.

Implementation
To fix this, you can set the default value of my_list to None and then initialize a new list inside the function if my_list is None.
'''

def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

'''
Explanation
The function format_greeting uses curly braces {} for string formatting but doesn't use the f string or format method to properly format the string.

Implementation
To fix this, use an f-string or the str.format method.
'''

def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."

# Review 3
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count
    
'''
Explanation
The Counter class has a class attribute count and the __init__ method attempts to increment this count.
This leads to each instance having its own count attribute starting from 0.

Implementation
To fix this, you should use the class attribute directly.
'''

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def get_count(self):
        return Counter.count

# Review 4
import threading

class SafeCounter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

'''
Explanation
The SafeCounter class is not thread-safe. Multiple threads can increment self.count at the same time, leading to race conditions.

Implementation
To make it thread-safe, you can use a threading.Lock.
'''

import threading

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1

    return counts

'''
Explanation
The count_occurrences function has a bug where it uses =+ 1 instead of += 1. This would reset the count to +1 every time instead of incrementing it.

Implementation
To fix this, use += 1.
'''

def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
