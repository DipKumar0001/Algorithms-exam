def solve_postfix(expression):
    """
    Evaluates a Postfix (Reverse Polish Notation) expression.
    Input: String e.g., "1 2 + 3 *"
    Output: Result
    """
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            # If operand, push to stack
            stack.append(int(token))
        else:
            # If operator, pop two operands
            if len(stack) < 2:
                return "Error: Invalid Expression"
            
            val2 = stack.pop()
            val1 = stack.pop()
            
            if token == '+':
                stack.append(val1 + val2)
            elif token == '-':
                stack.append(val1 - val2)
            elif token == '*':
                stack.append(val1 * val2)
            elif token == '/':
                stack.append(val1 / val2)
            else:
                return f"Error: Unknown operator {token}"
                
    if len(stack) != 1:
        return "Error: Malformed expression"
        
    return stack[0]

if __name__ == "__main__":
    # Test case from prompt: 1 2 + 3 * 6 + 2 3 + /
    # Logic:
    # 1 2 + -> 3
    # 3 * -> 3 * 3 = 9
    # 6 + -> 9 + 6 = 15
    # 2 3 + -> 5
    # / -> 15 / 5 = 3
    
    expr = "1 2 + 3 * 6 + 2 3 + /"
    print(f"Evaluating: {expr}")
    result = solve_postfix(expr)
    print(f"Result: {result}")
    
    user_expr = input("\nEnter your postfix expression (space separated): ")
    if user_expr:
        print(f"Result: {solve_postfix(user_expr)}")
