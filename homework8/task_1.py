def html_teg(function):
    def html_wrapper():
        asd = function()
        return f"<html>{asd}<html>"
    return html_wrapper()



@html_teg
def say_hello():
    hello_1 = input("Введите нечто, что хотите заковать в html: ")
    return hello_1

print(say_hello)