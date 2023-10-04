#-----------------------------------------------------------------------------------------------------------------------
# 7.3 Getter Setter and Read only property Using Property Decorator
#-----------------------------------------------------------------------------------------------------------------------
class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    @property                                   # Method converted to Property. Getter without setter. Read only mode.
    def age(self):
        return self._age

    @property                                   # Method converted to Property. Getter without setter. Read only mode.
    def money(self):
        return self.__money

    @money.setter                               # Setter for the money getter. Read only mode.
    def money(self, new_value):
        if new_value > 0:
            self.__money += new_value
        else:
            print('Salary can\'t be 0.')



jems = User('Jems', 23, 12000)

#print(jems.name)       # No accessible, because protected. But with _name possible to access.
#print(jems.age)        # No accessible, because protected. But with _age possible to access.
#print(jems.money)      # No accessible, because private. Even with __money not possible to access.

#If we create a method for age, then it will be accessible.
#print(jems.age())
#But see, there is () after age. That means we are using the age as a method.

#Now if we add [@property] decorator just above the age method snippet, then the method age() will function like a
#property of the class. And it will be accessible even without ().
print(jems.age)
print(jems.money)

#Remember, this age and money were properties, but protected and private. And was not easily accessible.
#Then we created methods for them and created a way to access them.
#Then again we converted them back to properties, and they are now accessible. This process is actually called [getter].
#Using getter, we may have access, but only in [Read only] mode. That means, we can read them, but can't write them.

jems.money = 500
#Without the setter, this line should give us error.
#So we need setter to write them, or update the value of them.
#Geater to get them and setter to set them, easy to understand.

#After creating the setter, if we try to update the money with new value, it will not show error.
#Rather the balance will be updated. Let's see the balance.
print(jems.money)

#-----------------------------------------------------------------------------------------------------------------------
