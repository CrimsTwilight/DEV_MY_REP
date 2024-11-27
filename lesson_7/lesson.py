def outer_function(x):
    def inner_function (y):
        return x + y
    return inner_function

closure = outer_function (10)
print(closure(5))


def select(input_func):
    def output_func():
        print("*****************")
        input_func()
        print("*****************")
    return output_func

@select
def hello():
    print("Hello from the original function")

hello()
