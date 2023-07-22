def foo(text):
    """большая буква"""
    return text.upper()

def foo2(text):
    """каждое новое слово с большой буквы"""
    return text.title()

user_input = input("Введите текс")


print(foo(user_input))
print(foo2(user_input))