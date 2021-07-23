# Determine if the largest number in an unordered list is larger than 100
unordered_list = [1000, 393, 304, 40594, 235, 239, 2, 4, 5, 23095, 9235, 31]

# We start by ordering the list
ordered_list = sorted(unordered_list)

# Then we retrieve the last element of the ordered list
largest_number = ordered_list[-1]

# And we print the result
if largest_number > 100:
  print("The largest number in the list is larger than 100")
else:
  print("The largest number in the list is smaller than 100")
