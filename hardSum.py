def calc(numbers):
    if not numbers:
        return 0
    return int(numbers[0]) + calc(numbers[1:])

nums = input().split()
print(calc(nums))