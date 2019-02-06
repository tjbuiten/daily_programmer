print("Please state your name, age and reddit username seperated by a comma and an empty space (, ) :")
name, age, username = input().split(', ')
print("your name is %(n)s, you are %(a)s years old, and your username is %(u)s" % {'n': name, 'a': age, 'u': username})
