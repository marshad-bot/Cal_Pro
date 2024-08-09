import streamlit as st
import math

# Set up the Streamlit app
st.title('Scientific Calculator')

# Define the scientific calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error: Logarithm of non-positive number"

# Create inputs for the user
num1 = st.number_input('Enter the first number:', value=0.0)
operation = st.selectbox('Choose an operation:', ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Square Root', 'Sine', 'Cosine', 'Tangent', 'Logarithm'])

# Handle operations with one or two numbers
if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Logarithm']:
    num2 = st.number_input('Enter the second number:', value=0.0)

if st.button('Calculate'):
    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)
    elif operation == 'Power':
        result = power(num1, num2)
    elif operation == 'Square Root':
        result = sqrt(num1)
    elif operation == 'Sine':
        result = sin(num1)
    elif operation == 'Cosine':
        result = cos(num1)
    elif operation == 'Tangent':
        result = tan(num1)
    elif operation == 'Logarithm':
        base = st.number_input('Enter the base for the logarithm:', value=10.0)
        result = log(num1, base)
    
    st.write(f'Result: {result}')
