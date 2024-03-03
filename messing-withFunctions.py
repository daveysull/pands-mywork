'''
def cube(number):
    print(number)
    return (number **3)

answer = cube(23)
print(f'we got {answer}')


#Unnamed Args
def fun1 (*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a", "b", "c")'''

def ave(*values):
    number_of_values = len(values)
    sum = 0
    for value in values:
        sum += value

    average = sum / number_of_values
    return average

print(round(ave(1,23,23,44,45,16)))
    