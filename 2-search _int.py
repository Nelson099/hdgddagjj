def find_first_occurrence(my_list, num):
    
    for i in range(len(my_list)):
        if my_list[i] == num:
            return i
    return -1

if __name__ == "__main__":
    my_list = [5, 3, 7, 1, 9, 2,8]
    num = 9
    index = find_first_occurrence(my_list, num)
    if index != -1:
        print(f"The first occurrence of {num} in the list is at index {index}.")
    else:
        print(f"{num} is not in the list.")
