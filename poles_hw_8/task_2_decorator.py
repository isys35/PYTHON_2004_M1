
def get_input_func():
    user_input = input('Введите строку для обертки: ')
    return user_input

def html_decorator(function):
    def html_wrapper():
        return f"<html>{function}<html>"
    return html_wrapper()


print(html_decorator(get_input_func()))

