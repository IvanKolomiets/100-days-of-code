import time
current_time = time.time()
print(current_time)

def speed_decorator(function):
    def wrapper():
        current_time = time.time()
        function()
        print(f"{function.__name__} run speed: {time.time() - current_time}")
        
    return wrapper

@speed_decorator
def fast_function():
    for i in range(0,1000000):
        i*i

@speed_decorator
def slow_function():
    for i in range(0,10000000):
        i*i

fast_function()
slow_function()