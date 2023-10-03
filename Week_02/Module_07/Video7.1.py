#-----------------------------------------------------------------------------------------------------------------------
# 7.1 Operator overloading and method overriding
#-----------------------------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        return f'A person can eat any food of his choice.'

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        return f'Cricketers food charts are well maintained and with full of nutrition.'

    def exercise(self):
        return f'Cricketers are obliged to do physical exercise to maintain fitness.'

    def __add__(self, other):
        return self.name + other.name, self.age + other.age, self.height + other.height, self.weight + other.weight, self.team

    def __mul__(self, other):
        return self.weight * other.weight


sakib = Cricketer('Sakib Al Hasan', 38, 68, 91, 'Bangladesh')
print(sakib.eat())
print(sakib.exercise())
print('---------------------------------')

#-----------------------------------------------------------------------------------------------------------------------
"""
See the code above. Person is a parent class and cricketer is a child class. If we don't write the [eat] method under 
the child class, and call the [eat] method, then the output will come from the parent class. And we'll see as shown 
below. 

A person can eat any food of his choice.

But if we write the eat method under the child class, and call the [eat] method, then the output will come from the 
child class. And we'll see as shown below.

Cricketers food charts are well maintained and with full of nutrition.Cricketers food charts are well maintained and 
with full of nutrition.

This is called Method Overriding. Here [eat] method of child class is overriding the [eat] method of the parent class.

On the other hand see the [exercise] method in the  parent class. There [raise NotImplementedError] is mentioned. That
means, it's actually forcing the child class to create [exercise] method. Otherwise it will show NotImplementedError. 

#To Learn more, visit (https://www.geeksforgeeks.org/method-overriding-in-python/).
"""
#-----------------------------------------------------------------------------------------------------------------------

print(45 + 65)
print('Robert' + 'Bosch')
print([1, 2, 3] + [4, 5, 6])

"""
See these three lines. The operator sign [+] is being used in 3 different ways. The [+] operator sign is adding two
numbers, two strings and two lists. This is called 'Operator Overriding'.

We can do this simple operator overriding, just because these data types are predefined data types. But if we want to
use the same operator overriding for two object of a class which is created by us?

Let's see another example.
"""
#-----------------------------------------------------------------------------------------------------------------------

mushfiq = Cricketer('Mushfiqur Rahman', 35, 67, 78, 'Bangladesh')

print(sakib + mushfiq)

"""
Now let's create another player using the [Player] class. And now I want to add two players using [+] sign. See the 
output we have got.
#unsupported operand type(s) for +: 'Cricketer' and 'Cricketer'

So to do the operator overriding, we'll have to create our own operator overriding method. We'll create this using
[def __add__(self, other)]. After that the output will come up exactly how we constructed the output in the method.

('Sakib Al HasanMushfiqur Rahman', 73, 135, 169, 'Bangladesh')

Not only + sign, we can design Operator Overriding method for a lot of operators, like - * / and many more.
#To Learn more, visit (https://www.geeksforgeeks.org/operator-overloading-in-python/).
"""
#-----------------------------------------------------------------------------------------------------------------------
