for skaitlis in range(1, 101):
    if skaitlis%3==0 and skaitlis%5==0:
        print("FizzBuzz")
    elif skaitlis%3==0:
        print("Fizz")
    elif skaitlis%5==0:
        print("Buzz")
    else:
        print("skaitlis")

