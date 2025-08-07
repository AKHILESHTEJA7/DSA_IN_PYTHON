# what is Recursion: 
# ANS: where a function call itself to solve a problem. it has a base case and recursive case.
# BASE CASE: This is the condition that terminates the recursion.
# RECURSIVE CASE: The recursive call, invoking itself with a modified input that moves closer to the base case.

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
