# #출력할 디자인이 저장된 리스트
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# #남은 게 없을 때까지 디자인을 출력합니다

# def print_models(unprinted_designs, completed_models):

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(compledted_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

list = ["A", "B", "C"]

def show_messages(x):
    # b=[]
    # while x:
    #     a = x.pop(0)
    #     b.append(a)
    # print(b)
    for i in x:
        print(i)

show_messages(list)
