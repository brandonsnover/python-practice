# Write a method that takes in a number and returns the number times two. Then run the method and print the result.
def double(num):
  return num * 2

print(double(8))

# Write a method that takes in a string and returns the string with all capital letters. Then run the method and print the result.
def all_caps(word):
  return word.upper()

print(all_caps("string"))

# Write a method that takes in two numbers and returns the first number subtracted by the second. Then run the method and print the result.
def difference(num1, num2):
  return num1 - num2

print(difference(5, 2))

# Write a method that takes in a number and returns the number times itself. Then run the method and print the result.
def square(number):
  return number * number

print(square(8))

# Write a method that takes in a string and returns the first letter of the string. Then run the method and print the result.
def first_letter(string):
  return string[0]

print(first_letter("hello"))

# Write a method that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the method and print the result.
def string_combine(s1, s2, s3):
  return f"{s1} {s2} {s3}"

print (string_combine("hello", "from", "python"))

# Write a method that takes in a number and returns the number as a string. Then run the method and print the result.
def num_to_string(num):
  return str(num)

print(num_to_string(7))

# Write a method that takes in a string and returns the string repeated 5 times. Then run the method and print the result.
def string_five(string):
  return string * 5

print(string_five("hello"))

# Write a method that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the method and print the result.
def avg_three(num1, num2, num3):
  return (num1 + num2 + num3) / 3

print(avg_three(2, 3, 4))

# Write a method that takes in a number and returns the number times 10 plus 30. Then run the method and print the result.
def ten_x_plus_thirty(num):
  return num * 10 + 30


print(ten_x_plus_thirty(8))