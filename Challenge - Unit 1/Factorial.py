def factorial(n):

  # base case: if `n` is 0 or 1
  if n < 1:
    return 1

  # use the recurrence relation
  return n * factorial(n - 1)

n = int(input('Enter the Number for Factorial:'))
print(f'The Factorial of {n} is', factorial(n))
