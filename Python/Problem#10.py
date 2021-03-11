"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

# Simple solution
import time

def job_scheduler(func, delay):
    time.sleep(delay / 1000) # miliseconds
    func()


def print_hello():
    print(f"Hello World!")

print(time.time())
job_scheduler(print_hello, 5000)
print(time.time())


# with Multithreading
import time
import threading

def job_scheduler(func, delay, id):
    print(f"Schedule Job for Thread: {id}")
    time.sleep(delay / 1000) # miliseconds
    func(id)
    print(f"Finished Job for Thread: {id}")


def print_hello(id):
    print(f"Hello from Thread: {id}")

print("Main Thread starts Job Schdeuler")
for i in range(1, 6):
    t = threading.Thread(target=job_scheduler, args=(print_hello, i*1000, i))
    t.start()

print("Main Thread finished")
