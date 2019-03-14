import operator

operator_dictionary = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

operator = input("Please state the function you want to execute, available options consist of: \n + \n - \n * \n / \n ^ \n")
numbers = list(map(int, input("Please give the numbers you want to execute the function on seperated by a comma and an empty space (, ) : \n").split(', ')))

result = numbers.pop(0)

for number in numbers:
    result = operator_dictionary[operator](result, number)

print("Result: " + str(result))
