# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def problem(n: int):
    return sum([number for number in range(n) if number % 3 == 0 or number % 5 == 0])


print(problem(1000))

# Instagram, ProjectEuler.net: ilya._romanovich
# Telegram: @kizilov_elijah