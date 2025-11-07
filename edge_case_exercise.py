def move(my_list, direction):
    index_of_one = my_list.index(1)

    if direction == "right":
        if my_list[-1] == 1:
            return my_list
        else:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1

    elif direction == "left":
        if my_list[0] == 1:
            return my_list
        else:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1

    return my_list
