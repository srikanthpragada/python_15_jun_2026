def wish(user="Guest", message='Hello'):
    print(message, user)


# Positional arguments
wish('Martin')
wish('Micheal', "Hi")
wish()

# Keyword arguments
wish(message='Hello', user='Micheal')
wish(user="Marshall")
wish(message="Hi")
