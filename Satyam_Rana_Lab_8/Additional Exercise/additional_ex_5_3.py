class Person:
    def __init__(self, name, age=-1):
        self.name = name
        self.age = age

    def hello(self, friend_name):
        friend_upper = friend_name.upper()
        if self.age == -1:

            print(f"Hello {friend_upper}, I am {self.name}")
        else:
            print(f"Hello {friend_upper}, I am {self.name} and I'm {self.age} years old")


man_1 = Person("Al", 31)
girl_1 = Person("Wanda")   

man_1.hello("Jack")
girl_1.hello("Jack")
