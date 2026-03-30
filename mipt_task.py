def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
year = 2027
print(f"Сумма цифр {year} года: {sum_digits(year)}")
