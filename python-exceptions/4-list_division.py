#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for idx in range(list_length):
        output = 0
        try:
            a = my_list_1[idx]
            b = my_list_2[idx]
            output = a/b
        except TypeError:
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            div_list.append(output)
    return div_list
