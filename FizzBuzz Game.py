# FizzBuzz game for numbers 1 to 20
for i in range(1, 21):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")
        
    else:
        print(i)
