
user_input = input("Enter characters and their counts separated by spaces: ")
input_list = user_input.split()
print(input_list)
output_string = ""

for i in range(0, len(input_list), 2):
    char = input_list[i]
    count = int(input_list[i+1])
    output_string += char * count

# Print the final output
print(output_string)
