class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        
        mapping = {')': '(', '}': '{', ']': '['}

        
        for char in s:
            
            if char in mapping:
                
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                
                stack.append(char)

        
        return not stack

if __name__ == "__main__":
    solution = Solution()
    
    
    user_input = input("Enter a string of parentheses: ")

    # Check if the input string is valid
    result = solution.isValid(user_input)
    print(result)  # Print True or False directly
