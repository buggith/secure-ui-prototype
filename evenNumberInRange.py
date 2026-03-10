def even_numbers(first, last):
    even = []
    for number in range(first, last):
        if number % 2 == 0:
            even.append(number)
    return even

print(even_numbers(4, 14))  # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))   # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))   # Should print [2, 4, 6]
