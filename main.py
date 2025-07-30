def add(numbers):
    
    
    temp = 0
    # This method will completely ignore the need to check the delimiter.
    # It would be better to iterate over each character to see if
    # it is an int or string. If it is then just convert it into
    # an int and just add it up. 
    for char in numbers:
        if char.isdigit():
            newnumber = int(char)
            temp = temp + newnumber
            
    return temp
            


result =  add("1,2,3")

print(result)
