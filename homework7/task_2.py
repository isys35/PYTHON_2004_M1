
def repeater(repeat):
    def decorator(function):
        def wrapper(*args):
            for i in range(repeat):
                print(f"{i+1}: ", end="")
                val = function(*args)
            return val
        return wrapper
    return decorator

@repeater(repeat=7)
def z_count(name):
    print(f"Привет {name}")

z_count("Сергей")