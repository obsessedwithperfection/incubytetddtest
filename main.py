def add(numbers):
    
    # We do not need this if statement
    # because the loop will never run of there is empty string.
    # if not numbers:
    #     return 0
    
    # bypassing any kind of delimeter
    
    temp = 0
    current = ""

    for char in numbers:
        if char.isdigit():
            current += char  # build number from consecutive digits
        else:
            if current:
                temp += int(current)
                current = ""

    # Add the last number (if the string ends with a digit)
    if current:
        temp += int(current)

    # print("mynumber =", mynumber)
    return temp


# def main():
    
#     test_cases = [
#         "1,2,3",        # Comma
#         "1;2;3",        # Semicolon
#         "1|2|3",        # Pipe
#         "1\n2\n3",      # Newlines
#         "1 2 3",        # Spaces
#         "1-2-3",        # Hyphen as delimiter (careful: may conflict with negative numbers)
#         "1:2:3",        # Colon
#         "1/2/3",        # Slash
#         "1#2#3",        # Hash
#         "1a2b3c4",      # Letters as delimiters
#         "1@2@3",        # Special characters
#         "100&200&300",  # Ampersand
#         "9*8*7",        # Asterisk
#         "1;22;3",        # 
#     ]
    
#     for numbers in test_cases:
#         print(numbers)
#         result = add(numbers)
#         print(result)

test_cases = {
    "1,2,3": 6,
    "1;2;3": 6,
    "1|2|3": 6,
    "1\n2\n3": 6,
    "1 2 3": 6,
    "1-2-3": 6,  # Will fail if negative numbers are not handled correctly
    "1:2:3": 6,
    "1/2/3": 6,
    "1#2#3": 6,
    "1a2b3c4": 10,
    "1@2@3": 6,
    "100&200&300": 600,
    "9*8*7": 24,

    # Edge / invalid / tricky cases
    # "1--2--3": "may fail due to negative number parsing",
    # "-1,-2,3": "should raise error or handle negatives",
    # "3.14,2.71": "will be treated as [3, 14, 2, 71] → sum = 90",
    # "1,002,3": 6,  # Parsed as 1, 2, 3
    # "": 0,
    # "abc": 0,
    # "1,,2": 3,  # Should still parse 1 and 2
}


def main():
    # for input_str, expected in test_cases.items():
    #         result = add(input_str)
    #         if result != expected:
    #             print("There is still a problem in the program")
    
            result = add("1&666&2&666&3")
            
            print(result)
    


main()


