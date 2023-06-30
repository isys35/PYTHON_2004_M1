# Homework-8: Task-2
"""
Напишите функцию-декоратор, чтобы она заключала возвращаемое значение упакованной функции в html теги.
Обернутая функция должна возвращать подобный результат:
    <html>hello<html>
"""


def html_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<html>{result}<html>"
    return wrapper


@html_decorator
def say_hello():
    return "hello"


if __name__ == '__main__':
    print(say_hello())

