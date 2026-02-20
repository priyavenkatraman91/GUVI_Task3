
#People age below 18
people=[{"name": "Bob", "age": 30},{"name": "Ani", "age": 15},
{"name": "Tom", "age": 10},{"name": "Sony", "age": 18},{"name": "Clara", "age": 51}]
minor = dict(map(lambda x: (x["name"], x["age"]),
                 filter(lambda x: x["age"] < 18, people)))
print("People age under 18 are \n",minor)

#product of the numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
Product = reduce(lambda x, y: x * y, numbers)
print("The product of the numbers ", numbers,"is ",Product)


# Suqare of even numbers

square =list(map(lambda x: x ** 2,filter(lambda x: x % 2 == 0, numbers)))
print("\n The square of even number from ", numbers, "are",square)

# Find whether the given string is a number
is_number = lambda n:(True if n.replace('.','',1).lstrip('-').isdigit() else False)
print("\nFind whether the given string is a number")
print("\n -2.5 is a number? ",is_number("-2.5"))
print("\n Priya is a number? ",is_number("Priya"))


from datetime import *
dt = datetime(2026, 2, 12, 8,30)
extract_ymd =lambda yd:(yd.year,yd.month,yd.day)
extract_year= lambda y:(y.year)
extract_month= lambda m:(m.month)
extract_day= lambda d:(d.day)
print("\n The year month and date form the given date is ",extract_ymd(dt))
print("\n The Yrar from the given date",extract_year(dt))
print("\n The Month from the given date",extract_month(dt))
print("\n The Day from the given date",extract_day(dt))

#Generate a fibbonacci series
from functools import reduce

fib = lambda n: reduce(
    lambda a, _: a + [a[-1] + a[-2]],
    range(n-2),
    [0, 1]
)[:n]

print("\n The fibonacci series is ",fib(7))