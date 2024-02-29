def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full.name.title()

#무한루프입니다!
while True:
    # print("\nPlease tell me your name:")
    # f_name = input("First name: ")
    # l_name = input("Last name: ")

    # get_formatted_name = get_formatted_name(f_name,l_name)
    # print(f"\nHello, {foratted_name}!")

    print("\nPlease tell me your name:")    
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break