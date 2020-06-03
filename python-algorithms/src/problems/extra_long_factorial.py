def extra_long_factorial(n):
    factorial = '1'
    for number in range(2, n + 1, 1):
        factorial = multiply_big_numbers(factorial, str(number))
    return factorial


def multiply_big_numbers(number1, number2):
    first_number_arr = string_to_number_array(number1)
    second_number_arr = string_to_number_array(number2)
    product_arrays = []
    for second_number_index in range(len(second_number_arr)):
        second_number_digit = second_number_arr[second_number_index]
        addition = 0
        product_array = [0] * second_number_index
        for first_number_index in range(len(first_number_arr)):
            first_number_digit = first_number_arr[first_number_index]
            product = (first_number_digit * second_number_digit) + addition
            addition = 0
            if product >= 10:
                addition = product // 10
            product_array.append(str(product % 10))
            if first_number_index == len(first_number_arr) - 1 and product >= 10:
                product_array.append(str(addition))
        product_arrays.append(product_array)
    return concat_products(product_arrays)


def string_to_number_array(string):
    number_array = list(map(lambda item: int(item), string))
    number_array.reverse()
    return number_array


def concat_products(products):
    concated_products = products[0]
    for product in products[1:]:
        len_diff = len(concated_products) - len(product)
        array_to_normalize = concated_products if len_diff < 0 else product
        array_to_normalize.extend(['0'] * abs(len_diff))
        concated_products = sum_products(concated_products, product)
    return ''.join(concated_products)[::-1]


def sum_products(product1, product2):
    sum_array = []
    addition = 0
    for i in range(len(product1)):
        number1, number2 = int(product1[i]), int(product2[i])
        sum = number1 + number2 + addition
        addition = 0
        if sum >= 10:
            addition = sum // 10
        sum_array.append(str(sum % 10))
        if i == len(product1) - 1 and sum >= 10:
            sum_array.append(str(addition))
    return sum_array
