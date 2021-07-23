# Determine the smallest number in an unordered list
unordered_list = [1000, 393, 304, 40594, 235, 239, 2, 4, 5, 23095, 9235, 31]

# We start by ordering the list
ordered_list = sorted(unordered_list)

# Then we retrieve the first element of the ordered list
smallest_number = ordered_list[0]

# And we print the result
print(f"The smallest number is: {smallest_number}")
