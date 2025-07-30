def add(numbers):
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

    return temp

result = add("1,22,3")
print(result)
