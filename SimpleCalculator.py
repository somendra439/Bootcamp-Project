# Step 1: Basic Arithmetic Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Step 2: Tokenize the Input Expression
def tokenize(expression):
    return expression.split()

# Step 3: Evaluate Postfix Expression Using Stack
def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    tokens = tokenize(expression)
    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            y = stack.pop()
            x = stack.pop()
            if token == '+':
                stack.append(add(x, y))
            elif token == '-':
                stack.append(subtract(x, y))
            elif token == '*':
                stack.append(multiply(x, y))
            elif token == '/':
                stack.append(divide(x, y))

    return stack.pop()

# Step 4: Infix to Postfix Conversion Using Shunting Yard Algorithm
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators = set(['+', '-', '*', '/'])
    stack = []
    output = []

    tokens = tokenize(expression)
    for token in tokens:
        if token not in operators:
            output.append(token)
        else:
            while (stack and stack[-1] in operators and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# Step 5: User Interface
def calculator():
    print("Simple Calculator")
    print("Enter 'exit' to quit")

    while True:
        expression = input("Enter expression in infix notation: ")
        if expression.lower() == 'exit':
            break
        try:
            postfix_expression = infix_to_postfix(expression)
            result = evaluate_postfix(postfix_expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

# Run the calculator
calculator()
