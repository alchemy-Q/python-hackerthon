# # Functions & Fibonacci Sequence
# # Question
# # Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
# #We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
# def fibonacci(n):
#   """
#   This function generates the Fibonacci sequence up to a specified term n using iteration.

#   Args:
#       n: The number of terms in the Fibonacci sequence.

#   Returns:
#       A list containing the Fibonacci sequence up to n terms.
#   """
#   if n <= 1:
#     # Complete here
#   else:
#     a, b = # complete here
#     for _ in range(2, n + 1):
#       c = a + b
#       # Complete here
#     return # add the variable to be returned

# # Get the number of terms from the user
# num_terms = int(input("Enter the number of terms: "))

# # Generate the Fibonacci sequence
# fibonacci_sequence = []
# for i in range(num_terms):
#   fibonacci_sequence.append(fibonacci(i))

# # Print the Fibonacci sequence
# print(fibonacci_sequence)

# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.


#THE ASSIGNMENT BEGINS FROM HERE

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # Start with the first two terms of the Fibonacci sequence

    # Generate Fibonacci sequence up to the specified term n
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Ask the user to input the value of n
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Call the function to generate the Fibonacci sequence
fib_sequence = generate_fibonacci_sequence(n)

# Print the generated Fibonacci sequence
print("Generated Fibonacci sequence up to term", n, ":", fib_sequence)
