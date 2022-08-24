def tags(res_tag):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f"<{res_tag}>{''.join(result)}</{res_tag}>"
        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
