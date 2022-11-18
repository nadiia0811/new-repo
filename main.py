a = int(input('Enter a number1: '))
b = int(input('Enter number2: '))
if a > b:
    (a, b) = (b, a)

while a <= b:
    print(a)
    a = a + 1



