# Write a while loop to print the numbers 1 through 10.
count = 1
while count <= 10:
  print(count)
  count += 1

# Write a while loop that prints the word "hello" 5 times.
count = 0
while count < 5:
  print("hello")
  count += 1

# Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".
while True:
  word = input("enter a word: ")
  if word == "stop":
    break

# Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.
count = 0
while count <= 100:
  print(count)
  count += 5

# Write a while loop that prints the number 9000 ten times.
count = 0
while count < 10:
  print(9000)
  count += 1

# Write a while loop that prints the numbers 50 to 70.
count = 50
while count <= 70:
  print(count)
  count += 1

# Write a while loop that prints the phrase "Around the world" 144 times.
count = 0
while count < 144:
  print("Around the world")
  count += 1

# Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.
while True:
  word = input("enter a word: ")
  if len(word) >= 5:
    break
