def string_to_ascii_array():
    # Take input string from the user
    input_string = input("Enter a string: ")
    
    # Convert each character to its ASCII value and store in a list
    ascii_values = [ord(char) for char in input_string]
    
    # Print the resulting array of ASCII values
    print("ASCII values:", ascii_values)

# Run the program
string_to_ascii_array()
