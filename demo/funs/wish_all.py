def wish_all(*users, message = "Hello"):
    for user in users:
        print(message, user)


wish_all("George",'Martin', "Scott", message = "Hi")
wish_all("George", "Scott")








