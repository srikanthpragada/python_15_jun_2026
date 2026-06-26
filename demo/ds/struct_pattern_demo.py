# Assume d may have any one of the following two structures
d = {'uname': 'Jack', 'email': 'jack@gmail.com'}
match d:
    case {'name': user}:
        pass
    case {'firstname': user}:
        pass
    case _:
        user = 'Unknown'

print(user)