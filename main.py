def add(numbers):
    temp = 0
    # I am adding this extra mynumbers to show how this program just retreive numbers
    # out of string without caring any kind of delimiter.
    mynumbers = []
    current = ""

    for char in numbers:
        if char.isdigit():
            current += char  # build number from consecutive digits
        else:
            if current:
                mynumbers.append(int(current))
                temp += int(current)
                current = ""

    # Add the last number (if the string ends with a digit)
    if current:
        mynumbers.append(int(current))
        temp += int(current)

    print("mynumber =", mynumbers)
    return temp


def main():
    
    test_cases = [
        "1,2,3",        # Comma
        "1;2;3",        # Semicolon
        "1|2|3",        # Pipe
        "1\n2\n3",      # Newlines
        "1 2 3",        # Spaces
        "1-2-3",        # Hyphen as delimiter (careful: may conflict with negative numbers)
        "1:2:3",        # Colon
        "1/2/3",        # Slash
        "1#2#3",        # Hash
        "1a2b3c4",      # Letters as delimiters
        "1@2@3",        # Special characters
        "100&200&300",  # Ampersand
        "9*8*7",        # Asterisk
        "1;22;3",        # Asterisk
    ]
    
    for numbers in test_cases:
        print("numbers =", numbers)
        result = add(numbers)
        print("sum =",result)
        print("-" * 50)



main()

