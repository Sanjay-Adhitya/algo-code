def fizzBuzz(n):
    # Write your code here
    for i in range(1,n):
        if (i%3) == 0 and (i%5) == 0:
            print("FizzBuzz")
            continue
        if (i%3) == 0 and (i%5) != 0:
            print("Fizz")
            continue
        if (i%3) != 0 and (i%5) == 0:
            print("Buzz")
            continue
        print(i)
fizzBuzz(15)