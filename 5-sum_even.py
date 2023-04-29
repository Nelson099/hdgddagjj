def sum_even_numbers(my_list):
    sum = 0
    for num in my_list:
        if num % 2 == 0:
            sum += num
    return sum

if __name__ == "__main__":
    my_list = [10,11,12,13,14,15,16,17,18,19,20]
    sum_even = sum_even_numbers(my_list)
    print(f"The sum of even numbers in {my_list} is: {sum_even}")
