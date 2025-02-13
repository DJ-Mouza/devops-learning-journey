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

test_result = (input("What is your test result?\n"))

new_test_result = int(test_result)

if new_test_result >= 40:                                                                                                         # If first condition is met proceed
    print("You have passed the first stage")

    exam_result = (input("What is your exam result?\n"))
    new_exam_result = int(exam_result)
    if new_exam_result >= 70:                                                                                                     # If second condition is met : new outcome
        print("Congratulation, you can now proceed to next level")
    else:                                                                                                                         # If second condition is not met: outcome
        print("You did not meet the requirement, please retake the exam!")                                                       
else:                                                                                                                             # If first condition is not met : outcome
    print("You were not successful on this occasion, you have to wait another month before you can re-take the test!")            

 