def pass_count(data, passmark=50):
    count = 0
    for marks in data.split(","):
        if int(marks) >= passmark:
            count += 1

    return count


print(pass_count("90,45,66,77,34"))
print(pass_count("90,45,88,60", passmark=70))
