# Nested if / else statement.


# conditional statement

#       if condition:
#         do this
#       else:
#         do this


# Nested if / else statement

#       if condition:
#         if another condition:
#            do this
#         else:
#            do this
#       else:
#         do this


# Practical example : Test and Exam.

# Conditional Logic for Test and Exam Result Evaluation

# Ask the user for their test result and store it as a string
test_result = input("What is your test result?\n")

# Convert the test result input to an integer
new_test_result = int(test_result)

# Check if the user has passed the first stage (test result >= 40)
if new_test_result >= 40:
    print("You have passed the first stage")

    # If the first condition is met, ask for the user's exam result
    exam_result = input("What is your exam result?\n")

    # Convert the exam result input to an integer
    new_exam_result = int(exam_result)

    # Check if the user has passed the exam (exam result >= 70)
    if new_exam_result >= 70:
        print("Congratulations, you can now proceed to the next level")  # User passed the exam
    else:
        print("You did not meet the requirement, please retake the exam!")  # User failed the exam

else:
    # If the user did not pass the test (test result < 40), inform them they need to wait
    print("You were not successful on this occasion. You have to wait another month before you can re-take the test!")
