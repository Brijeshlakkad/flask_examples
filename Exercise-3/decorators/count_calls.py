import functools

# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper_count_calls(*args, **kwargs):
#         wrapper_count_calls.num_calls += 1
#         print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
#         return func(*args, **kwargs)
#     wrapper_count_calls.num_calls = 0
#     return wrapper_count_calls
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
