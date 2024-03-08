def func1(humidity, val_set):
    if humidity < val_set:
        return 3

    return 1

def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    

        


def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2

    elif mode_type == "target":
        answer = func1

    elif mode_type == "minimum":
        answer = func3

    return answer