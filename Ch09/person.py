class Person:

    count = 0 ### !!!클래스 변수!!!

    def __init__(self, name, age, address): #생성자 역할
        self.name = name ###!!!인스턴스 변수!!!
        self.age = age
        self.address = address
        self.weight2 = [65,71,74,86,89,90,110]
        self.weight = 54 #공개속성
        self.height = 170
        self.__vision = 1.0 #private 속성
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1 

    def __getitem__(self, indx):
        return self.weight2[indx]

    def __call__(self):
        value = self.weight / (self.weight ** 2) 
        return round(value, 10)

    def __len__(self):
        return len(self.weight2)
    
    def __str__(self): #person 은 객체, 출력시 필요한 것은 스트링임
        return "{} {} {} 시력?{}".format(self.name, self.age, self.address, self.get_vision())

    def get_vision(self):
        return self.__vision

    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))

    def __eq__(self, other):
        return self.age == other.age
    
    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))


#########실행관련 코드는 person_test.py에서 확인하기 ########