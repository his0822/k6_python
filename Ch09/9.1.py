class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"식당이름 : {self.restaurant_name}, 요리종류 : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"레스토랑이 문을 열었습니다")

cla1 = Restaurant("맛집","한식")
cla1.describe_restaurant()
cla1.open_restaurant()

a1 = Restaurant("외식1번가","한식")
a2 = Restaurant("외식2번가","중식")
a3 = Restaurant("외식3번가","일식")

a1.describe_restaurant()
a2.describe_restaurant()
a3.describe_restaurant()

class User:

    def __init__(self, first_name, last_name, tel, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.age = age
        self.address = address


    def decsribe_user(self):
        print(f"사용자 정보 \n 1.이름:{self.first_name} {self.last_name}\n 2.연락처:{self.tel}\n 3.나이:{self.age}\n 4.주소:{self.address}")
        
    def greet_user(self):
        print(f"{self.first_name}{self.last_name}님 환영합니다!")

user1 = User("황","인상","010-111",80,"비밀")
user1.decsribe_user()
user1.greet_user()

