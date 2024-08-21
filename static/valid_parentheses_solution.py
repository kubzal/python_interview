def is_valid_parentheses(s: str) -> bool:
    # Dictionary to hold matching pairs of parentheses
    matching_parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Stack to keep track of opening parentheses
    stack = []
    
    # Traverse each character in the string
    for char in s:
        if char in matching_parentheses.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_parentheses.keys():
            # If the character is a closing bracket, check the stack
            if stack == [] or matching_parentheses[char] != stack.pop():
                # If stack is empty or does not match the correct opening bracket, return False
                return False
        else:
            # If an invalid character is found, return False (optional, depending on the problem's constraints)
            return False
    
    # If the stack is empty at the end, all the brackets are properly closed
    return stack == []

# Example usage:
print(is_valid_parentheses("()"))       # True
print(is_valid_parentheses("()[]{}"))   # True
print(is_valid_parentheses("(]"))       # False
print(is_valid_parentheses("([)]"))     # False
print(is_valid_parentheses("{[]}"))     # True
