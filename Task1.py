# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
# as attributes. Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.valid_name()
        self.lastname = lastname
        self.valid_surname()
        self.age = age
        self.valid_age()

    def valid_name(self):
        if self.firstname.isalpha():
            return self.firstname
        else:
            raise ValueError('Имя должно состоять из букв!')

    def valid_surname(self):
        if self.lastname.isalpha():
            return self.lastname
        else:
            raise ValueError('Фамилия должна состоять из букв!')

    def valid_age(self):
        if type(self.age) is not int:
            raise ValueError('Возраст должен иметь цифровой вид!')
        if self.age < 0 or self.age > 130:
            raise ValueError('Возраст должен быть в районе 0-130 лет!')
        else:
            return self.age

    def talk(self):
        print(f'Hello! My name is {self.firstname} {self.lastname} and I am {self.age} years old')


def main():
    firstname = 'Misha'
    lastname = 'Barkov'
    age = 19
    user = Person(firstname, lastname, age)
    user.talk()


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
