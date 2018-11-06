def typ(num):
    num_to_type = {1:int, 2:float, 3:str, 4:bool, 5:type(None)}
    return num_to_type[num]
def empty():
    pass

type_1 = typ(1)
print(isinstance(0, type_1))

type_2 = typ(2)
print(isinstance(0., type_2))

type_3 = typ(3)
print(isinstance("0", type_3))

type_4 = typ(4)
print(isinstance(False, type_4))

type_5 = typ(5)
print(isinstance(empty(), type_5))
