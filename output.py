input_list = [6, 1, 3, 9, 8, 5, 2]

# Sort the list with custom sorting key
output_list = sorted(input_list)


# Reverse elements from the 4th element (index 3) onward
start_index = 3
output_list[start_index:] = reversed(output_list[start_index:])




print(output_list)

