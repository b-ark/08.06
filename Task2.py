# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
import math
"""Реализовал через более точную формулу, поэтому не использовал атрибут age_factor.
 Формула не подходит для расчета возраста до 1 года"""


class Dog:
    def __init__(self, age):
        self.age = age
        self.valid_age()

    def valid_age(self):
        if not isinstance(self.age, (int, float)):
            raise ValueError('Возраст должен иметь цифровой вид!')
        if self.age < 1 or self.age > 20:
            raise ValueError('Возраст должен быть в районе 1-20 лет!')

    def human_age(self):
        return 16 * math.log(self.age) + 31


def main():
    dog_age = 1
    dog = Dog(dog_age)
    print(f"Человеческий возраст {dog.age} равен {dog.human_age()} возрасту собаки")


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
