# Program to check if a number is a power of 4
def powerOf4(number):
    # Check if number is positive and a power of 2 (only one bit set)
    if number <= 0 or (number & (number - 1)) != 0:
        return False

    count = 0
    # Count the number of zero bits before the only set bit
    while number > 1:
        number >>= 1
        count += 1

    # If count is even, then it's a power of 4
    return count % 2 == 0

# Input from the user
number = int(input("Enter your number: "))
if powerOf4(number):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')
