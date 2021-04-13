import functools

def decorator(func):

    def wrapper_fun(*args):
        nums=[x for x in args]
        value = func(*args)
        print(f"{func.__name__} function return sum of {nums}")
        print(f"The sum value {value} is raising 6 times")
        return (value * 6)
    return wrapper_fun

@decorator
def sum_num(a,b):
    return a+b

out=sum_num(6,4)
print(out)