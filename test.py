import random


def greet(name):
    return f"BoBoBo, {name}!"


def roll_dice(sides=6):
    return random.randint(1, sides)


def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


if __name__ == "__main__":
    print(greet("World"))
    print(f"You rolled a {roll_dice()}")
    print(" ".join(fizzbuzz(20)))
