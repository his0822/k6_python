available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
a1 = available_toppings
a2 = requested_toppings
a3 = []
if a3:
    for x in a3:
        print(f"Adding {x}.")
else:
    print("Are you sure you want a plain pizza?")


for x in a2:
    if x in a1:
        print(f"Adding {x}.")
    else:
        print(f"Sorry, we don't have {x}.")


print("\n""Finished making your pizza!")


