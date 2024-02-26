cars = ['bmw','audi','toyota','subaru']
# cars.sort()  --- 알파벳 순으로 정렬
# cars.sort(reverse = True)  ---- 알파벳 반대순으로 정렬
print(cars)
print(sorted(cars)) 
print(cars)
len(cars)
# print(cars[4])
print(cars[-1])
print("--------------------")
for car in cars: #확장형 for 문
    print(car)
    print(f'My car is a {car}.')
print("리스트 출력 완료")
