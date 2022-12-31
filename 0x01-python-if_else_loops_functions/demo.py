#!/usr/bin/python3
# Create a list of integers from 0 to 9
digits = list(range(10))

# Set the counter variables
i = 0
j = 1

# Start the loop
while i < 9:
  # Print the combination of the digits at indices i and j
    print(f"{digits[i]}{digits[j]}", sep=',')
  # Increment j and check if it needs to be reset
    j += 1
    if j == 10:
      j = i + 1
      i += 1
print()
