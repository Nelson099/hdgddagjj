def get_smallest_integer(my_list):
    smallest = my_list[0]
    for number in my_list:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == "__main__":
    my_list =[5,3,8,2,7,2]
    smallest = get_smallest_integer(my_list)
    print(f"The smallest in the list is: {smallest}")
    