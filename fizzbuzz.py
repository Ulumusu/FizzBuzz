def fizzbuzz(x):
    for x in range(1, x):
        if x%5==0 and x%3==0:
            print("FizzBuzz")
        elif x%3==0:
            print("Fizz")
        elif x%5==0:
            print("Buzz")
        else:
            print(x)


x=int(input("number\n"))
fizzbuzz(x)        
        
