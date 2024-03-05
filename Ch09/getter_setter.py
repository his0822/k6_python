class Shape:

    def __init__(self,base, height):
        self.__base = base
        self.__height = height
    
    ### getter, setter를 정의하는데 decorator 사용
    @property #decorator for getter
    def get_base(self):
        return self.__base

    def get_height(self):
        return self.__height
    
    @get_height.setter
    def set_height(self,value):
        self.__height = value

# 객체 생성
triangle = Shape(base=5, height=8)

# Getter를 사용하여 값 출력
print(f"Base: {triangle.get_base}")
print(f"Height: {triangle.get_height}")

# Setter를 사용하여 값 변경
triangle.set_height = 10

# 변경된 값 확인
print(f"Changed Height: {triangle.get_height}")

def get_data():
    return 1,2,3

_,a,b = get_data() ##첫번째꺼는 무시하고 두번째, 세번째만 쓰겠다

a=[1,2,3]
b=[11,22,33]
mylist = [*a,*b] ## 리스트병합
mylist2= a+b ## 병합
print(mylist)
print(mylist2)

c = ['a','b']
z1 = zip(a,b) #같은 위치끼리 묶음
z2 = zip(a,c)
z3 = zip(c,a) #배열 갯수가 다를경우 작은 갯수 기준
print(list(z1))
print(list(z2))
print(list(z3))


