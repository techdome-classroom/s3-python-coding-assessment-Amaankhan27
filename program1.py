class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        # Define a mapping of closing to opening parentheses
        mapping = {')': '(', '}': '{', ']': '['}

        # Iterate over each character in the string
        for char in s:
            # If the character is a closing parenthesis
            if char in mapping:
                # Pop the top element from the stack if it's not empty; otherwise, assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening parenthesis
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening parenthesis, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening parentheses were matched
        return not stack

if __name__ == "__main__":
    solution = Solution()
    
    # Take input from the user
    user_input = input("Enter a string of parentheses: ")

    # Check if the input string is valid
    result = solution.isValid(user_input)
    print(result)  # Print True or False directly
