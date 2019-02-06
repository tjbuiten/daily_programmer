name, age, username = input("Please state your name, age and reddit username seperated by a comma and an empty space (, ) :\n").split(', ')
print("your name is %(n)s, you are %(a)s years old, and your username is %(u)s" % {'n': name, 'a': age, 'u': username})

file = open("userData.txt", "a")
file.write("your name is %(n)s, you are %(a)s years old, and your username is %(u)s" % {'n': name, 'a': age, 'u': username})