import re

# Read the file
with open('input', 'r') as file:
	content = file.read()

# Extract all numbers using regular expression
numbers = re.findall(r'\d+', content)

# Convert the numbers to integers
numbers = [int(num) for num in numbers]

# Print the array of numbers
print(numbers)
