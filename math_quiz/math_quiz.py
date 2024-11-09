import random

def get_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    
    Args:
        min_value (int): The lower bound for the random integer.
        max_value (int): The upper bound for the random integer.
    """
    return random.randint(min_value, max_value)


def get_random_operator():
    """
    Selects a random mathematical operator from addition, subtraction, and multiplication.
    
    """
    return random.choice(['+', '-', '*'])


def perform_calculation(num1, num2, operator):
    """
    Performs a mathematical operation based on the operator provided.
    
    Args:
        num1 (int): The first number in the operation.
        num2 (int): The second number in the operation.
        operator (str): The operator for the operation ('+', '-', or '*').
        tuple: A tuple containing the problem string (e.g., "3 + 4") and the calculated answer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Perform calculation based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # For multiplication
        answer = num1 * num2
    
    return problem, answer


def math_quiz():
    """
    The main quiz game function that generates math problems and evaluates user input.
    
    The function asks the user five questions and checks if their answers are correct, and at last,
    the user's score is displayed.
    """
    score = 0  # Initialize score
    total_questions = 5  # The number of questions in the quiz (set to 5)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through each question
    for _ in range(total_questions):
        # Generate random numbers and an operator for each question
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)  # max_value should be an integer, so using 5
        operator = get_random_operator()

        # Get the math problem and correct answer
        problem, correct_answer = perform_calculation(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        
        # Ask user for input and handle potential invalid input
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break  # Exit loop once a valid input is given
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1  # Increment score for correct answer
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Output the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")
    print("Thanks for playing!")


# Run the quiz game if this script is being executed directly
if __name__ == "__main__":
    math_quiz()