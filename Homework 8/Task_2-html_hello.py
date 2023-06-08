def html_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<html>{result}<html>"
    return wrapper


@html_decorator
def say_hello():
    return "hello"


print(say_hello())
