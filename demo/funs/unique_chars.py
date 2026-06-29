def unique_chars(*names):
    unique_chars = set()
    for name in names:
        unique_chars = unique_chars | set(name)

    return "".join(unique_chars)


print(unique_chars("George","Martin","Scott"))
print(unique_chars("Mark","Jack"))

