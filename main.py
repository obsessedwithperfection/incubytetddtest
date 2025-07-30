import re

def add(numbers):
    
    # We do not need this if statement
    # because the loop will never run of there is empty string.
    # if not numbers:
    #     return 0
    
    # bypassing any kind of delimeter
    
    
    # Check for custom delimiter
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]  # Remove leading "//"
        
        numbers = parts[1]
        
        # Here it provides the ability to have multiple delimiters
        # in this form “//[delim1][delim2]\n”.
        if delimiter.startswith("["):
            delimiters = re.findall(r'\[(.*?)\]', numbers)
            for delim in delimiters:
                numbers = numbers.replace(delim, ",")
        else:
            numbers = numbers.replace(delimiter, ",")
                
                
        print(numbers)
        # Support delimiters like "//;\n1;2"

    
    # print(s)  # Output: 1,2,3
    
    temp = 0
    current = ""

    for index, char in enumerate(numbers):
        
        
        if char.isdigit():
            if(numbers[index-1] == "-"):
                # Found a negative number. Therefore stopping the program"
                raise ValueError("Negative numbers not allowed")
            current += char  # build number from consecutive digits
        else:
            if current:
                num = int(current)
                # Here it ignores Number bigger than 1000
                if num <= 1000:
                    temp += num
                current = ""
                

    # Add the last number (if the string ends with a digit)
    if current:
            num = int(current)
            # Here it ignores Number bigger than 1000
            if num <= 1000:
                temp += num

    return temp


test_cases = {
    "1,2,3": 6,
    "1\n2\n3": 6,
    "//,\n1,2,3": 6,
    "//;\n1;2;3": 6,
    "//|\n1|2|3": 6,
    "//\\n\n1\n2\n3": 6,     # Note: Python treats "\n" as newline, this is already actual newline
    "// \n1 2 3": 6,
    "//-\n1-2-3": 6,         # Will fail if negative numbers are not handled correctly
    "///\n1/2/3": 6,
    "//#\n1#2#3": 6,
    "//a\n1a2a3a4": 10,
    "//@\n1@2@3": 6,
    "//&\n100&200&300": 600,
    "//*\n9*8*7": 24,
    "//&666&\n1&666&2&666&3": 6,
    "//abc\n10abc20abc30": 60,

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
    
            # result = add("//&666&\n1&666&2&666&3")
            # result = add("//[;[{}]'/.][*]\n1;[{}]'/.2*3")
            result = add("//[;[{}]'/.][*]\n1;[{}]'/.2*32")
            # result = add(     "//1\n11213")
            # result = add("1,1002,3")
            # result = add("2,1001")
       
            # just remove the delimiter initially by replacing delimiter with ,
            print(result)
    


main()







