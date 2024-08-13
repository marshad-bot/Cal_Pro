import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Select operation
operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write(f"Result: {result}")
