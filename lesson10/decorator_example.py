def my_function(another_function):
    another_function()


@my_function
def func1():
    print("Hello World")