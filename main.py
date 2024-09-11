def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b != 0:
    return a / b
  else:
    return "Division by zero error"


if __name__ == "__main__":
  print(add(10, 5))
  print(subtract(10, 5))
  print(multiply(10, 5))
  print(divide(10, 0))
