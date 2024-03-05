from person import Person

Person('guest',11, 'jeju')


new_person = Person('hong',20, 'busan')
other_person = Person('hwnag',20,'seoul')
print(f"person 객체의 나이는 {new_person.age:5}***")
print("객체의타입은 {}입니다".format(isinstance(new_person,Person)))
      

print(new_person == other_person)

print(f"현재의 체중은 {new_person[2]} 입니다")

print("이 사람의 이름은 {}입니다".format(new_person.name))

print(f"이 사람의 몸무게는 {new_person.weight}입니다.")
print(f"이 사람의 체질량은 {new_person()}입니다.")
print("시력은 {}".format(new_person.get_vision()))
new_person.show_person_vision()

print("1 : "+str(new_person))
print("2 : "+ new_person.__str__())
print("3 : ")
print(new_person) # 자동호출

print(f"리스트길이 {len(new_person)}")

print(f"총 {Person.count}개의 객체가 생성됨")
print(f"다르게 총 {new_person.count}개의 객체가 생성됨")
print(f"또다르게 총 {other_person.count}개의 객체가 생성됨") 
## 클래스에 있는 클래스변수(자바에서 필드)는, 그 클래스 내에 생성된 객체들이 공유해서 사용. 

my_list = [1,2,3,4]
print(len(my_list))
 

