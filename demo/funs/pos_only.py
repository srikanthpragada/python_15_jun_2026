# Positional only arguments
def wish(name, message, /):
    print(message, name)


wish("Andy","Hi")
#wish(message="Hello", name="Jack")
