def reverse_words(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_string = "javed khan"
output_string = reverse_words(input_string)
print(output_string)  # Output: "devaj nahk"

