# Nick Crabb

# Every company needs to consider the security of their information systems.
# This program is a basic security questionnaire a company could use in
# determining whether they are doing proper information security practices.
# The security professional is asked five simple information security related
# questions.
# The user needs to respond yes or no to each question.
# For "yes" responses, the information security control is considered
# completed.
# For "no" responses the information security control is considered not
# completed.
# These responses are added and subtracting to present several different
# scores at the end of the program.
# Additionally, the percentage complete is computed.
# As well as, several other statistical functions are computed.
# Although it is based in five simple questions, it could be expanded to
# consider much more detailed information security requirements.

# printing the Assessment portal that my dads clients will have to take before
# he helps them with their company.
# Printing main throughout the whole code.
def main():
    print("Welcome to my Integration Project!")

def Question_num(number):
    print("Question " + number + "!")

def num_complete(completed):
    return completed + 1

def num_not_completed(not_completed):
    return not_complete + 1

#def numbers(limit):


main()
print("Assessment Portal")

print("This assessment will help you determine whether your company "
          "does basic information security practices.")


# The company will have to input their company name.
input("Enter Company Name: ")

# The company will have to input their company email.
company_email = input("Enter Company email:")
# Declaring final score, completed, and not complete so we can add up the
# scores at the end and view the percentages.
final_score = 0
completed = 0
not_complete = 0

# Code helped from my dad and
# https://www.w3schools.com/python/python_conditions.asp

# Declaring each question so the client knows how many questions there are.
Question_num("One")
# printing each question that the client will have to answer.
print("Do you have inventory software?")
# Having the client input either yes or no.
answer = input("Enter yes or no: ")
while answer != "yes" or "no":
    if answer == "yes":
        print("Complete")
        completed = num_complete(completed)
        break
    elif answer == "no":
        print("Not Complete")
        break
        not_complete = num_not_completed(not_complete)
    elif answer != "yes" or "no":
        print("invalid statement, try again")
        answer = input("Enter yes or no: ")


Question_num("Two")
print("Do you identify and fix vulnerabilities?")
answer = input("Enter yes or no: ")
while answer != "yes" or "no":
    if answer == "yes":
        print("Complete")
        completed = num_complete(completed)
        break
    elif answer == "no":
        print("Not Complete")
        break
        not_complete = num_not_completed(not_complete)
    elif answer != "yes" or "no":
        print("invalid statement, try again")
        answer = input("Enter yes or no: ")


Question_num("Three")
print("Do you have dedicated admin accounts?")
answer = input("Enter yes or no: ")
while answer != "yes" or "no":
    if answer == "yes":
        print("Complete")
        completed = num_complete(completed)
        break
    elif answer == "no":
        print("Not Complete")
        break
        not_complete = num_not_completed(not_complete)
    elif answer != "yes" or "no":
        print("invalid statement, try again")
        answer = input("Enter yes or no: ")


Question_num("Four")
print("Do you use updated and supported anti-virus or anti-malware solutions?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("Complete")
    completed = num_complete(completed)
elif answer == "no":
    print("Not Complete")
    not_complete = num_not_completed(not_complete)

Question_num("Five")
print("Is the antivirus solution centrally managed and logged?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("Complete")
    completed = num_complete(completed)
elif answer == "no":
    print("Not Complete")
    not_complete = num_not_completed(not_complete)

Question_num("Six")
print("Do you make backups of your sensitive information?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("Complete")
    completed = num_complete(completed)
elif answer == "no":
    print("Not Complete")
    not_complete = num_not_completed(not_complete)
if answer == "yes":
    print("Do you encrypt your backups?")
    answer = input("Enter yes or no: ")
    if answer == "yes":
        print("Complete")
        completed = num_complete(completed)
    elif answer == "no":
        print("Not Complete")
        not_complete = num_not_completed(not_complete)

Question_num("Seven")
print("Do you require multi-factor authentication for all access?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("Complete")
    completed = num_complete(completed)
elif answer == "no":
    print("Not Complete")
    not_complete = num_not_completed(not_complete)

Question_num("Eight")
print(
    "Do you have an inventory of hardware, cloud instances, virtual "
    "and physical servers, network devices, & wireless access points?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("Complete")
    completed = num_complete(completed)
elif answer == "no":
    print("Not Complete")
    not_complete = num_not_completed(not_complete)

# Printing the end score of the completed tasks.
print("Completed:", completed)
# printing the end score of the not complete tasks.
print("Not Completed:", not_complete)
# Subtracting the complete with the not complete to show the final score.
final_score = completed - not_complete
print("Final Score: ", final_score)

# Showing the total amount of questions answered.
print("You answered", (completed + not_complete) ** 1, "Questions!")
# Using sep to help concatenate the percentage sign and the final answer
# together for the percentage complete.
print("Percent Complete %", completed / 8 * 100, sep='')
# Using sep to help concatenate the percentage sign and the final answer
# together for the percentage not complete.
print("Percent Not Complete %", not_complete / 8 * 100, sep='')
# Using floor division to help the final code to round to the nearest ratio.
if completed >= 8:
    print("Everything Complete!")
    print("Great Job!")
else:
    print("Rounded Ratio", (completed / 8 * 100) // (not_complete / 8 * 100))
# Using Modulus to get the ratio remainder in the final code.
if completed == 8:
    print("Great Job!")
else:
    print("Ratio Remainder", (completed / 8 * 100) % (not_complete / 8 * 100))
# Using the end = operator to conclude the code.
print("Assessment ", end="completed!")
