motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append("GM")
motorcycles.append("ducati")
print(motorcycles)
motorcycles.insert(1,"Samcheonri")
print(motorcycles) 
del motorcycles[0]
print(motorcycles)

popped_motor = motorcycles.pop(1)
print(motorcycles)
print(popped_motor)

first_owned = motorcycles.pop(0)
print(f"The first motorcycles I owned was a {first_owned.title()}.")

motorcycles.remove("ducati")
print(motorcycles)

