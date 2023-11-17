for l in list(range(31)):
    if l % 15 ==0:
        print("FizzBuzz")
    elif l % 5 == 0:
        print("Buzz")
    elif l % 3 == 0:
        print("Fizz")
    else:
        print(l)