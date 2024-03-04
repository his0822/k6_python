class Dog:
    """Class representing a dog"""

    def __init__(self,name, age):
        ## Initializing name and age properies
        self.name = name #속성 -> 자바의 클래스 필드
        self.age = age
        self.__price = 1000
    ##self 는 필수 파라미터,

    def sit(self):
        """sitting"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """roll over"""
        print(f"{self.name} rolled over!")


dog = Dog()
print(dir(dog))
print(dir(Dog))

my_dog = Dog('Willie', 6) ##constructor call
##생성자 호출 -> 인스턴스 생성 -> __init__
my_dog.sit()


print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

