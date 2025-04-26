def is_disarium(num):
    digits = str(num)
    total = 0
    for index, digit in enumerate(digits):
        total += int(digit) ** (index + 1)
    return total == num
def find_disarium(start, end):
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=" ")
find_disarium(1, 1000)