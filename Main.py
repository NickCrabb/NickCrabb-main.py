"""
My awesome Integration project.
"""
__author__ = "Nick Crabb"


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
    # Creating a table of contents
    """
    Table of Contents
    :return:
    """
    done = 0
    # presetting done so scores can be calculated.
    not_done = 0
    # presetting not done so scores can be calculated.
    get_info()
    # Gathering the companies basic information
    ask_questions(done, not_done)
    # Giving the quiz taker 8 helpful questions for their company, done adds
    # a point if the answer input is yes, and not done adds one point if the
    # answer input is no.


def get_info():
    """
    Getting to know the company
    :return:
    """
    print("Assessment Portal")
    # The beginning of my assessment portal.
    print("")
    # Spacing out the lines for organization.
    print("This assessment will help you determine whether your company "
          "does basic information security practices.")
    # Telling the company what this assessment is for.
    input("Enter company name: ")
    # The company will have to input their company name.
    input("Enter company email: ")
    # The company will have to input their company email.
    input("Enter number of employees: ")
    # Number of workers in the company


def ask_questions(done, not_done):
    """
    Getting the Information
    :param done:
    :param not_done:
    :return:
    """
    # Declaring final score, completed, and not complete so we can add up the
    # scores at the end and view the percentages.
    # Code helped from my dad,
    # https://www.w3schools.com/python/python_conditions.asp, the POGILS, and
    # Paulo, the teacher assistant.
    # Declaring each question so the client knows how many questions there are.
    print("Question One!")
    # Starting the code off with question one.
    print("Do you have inventory software?")
    # Giving the quiz taker the first question.
    response = input("Enter yes or no: ")
    # Starting the IF, ELIF statement to determine whether the question is a
    # yes or no.
    validate = True
    # Giving the while loop validation.
    while validate:
        # Starting the while loop.
        if response == "yes":
            # Showing what would happen if yes is inputted.
            print("Complete!")
            # Printing complete.
            done += 1
            # Adding one to completed.
            validate = False
        elif response == "no":
            # Determining what is going to happen when the input is no.
            print("Incomplete")
            # Printing incomplete.
            not_done += 1
            # Adding one to not complete.
            input("What are you doing to improve this: ")
            # Having the user input what they are doing to improve their
            # company.
            validate = False
        elif response != "yes" or "no":
            # If the user doesn't input yes or no the program will ask them
            # to input yes or no again.
            print("invalid statement, try again")
            # Printing; invalid statement, try again.
            response = input("Enter yes or no: ")
            # Asking the user to input yes or no again.
    print("")

    print("Question Two!")
    print("Do you identify and fix vulnerabilities?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")

    print("Question Three!")
    print("Do you have dedicated admin accounts?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")

    print("Question Four!")
    print("Do you use updated and supported anti-virus or anti-malware "
          "solutions?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")

    print("Question Five!")
    print("Is the antivirus solution centrally managed and logged?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")

    print("Question Six!")
    print("Do you make backups of your sensitive information?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")
    print("Question Seven!")

    print("Do you require multi-factor authentication for all access?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")

    print("Question Eight!")
    print("Do you have an inventory of hardware, cloud instances, virtual "
          "and physical servers, network devices, & wireless access points?")
    response = input("Enter yes or no: ")
    validate = True
    while validate:
        if response == "yes":
            print("Complete!")
            done += 1
            validate = False
        elif response == "no":
            print("Incomplete")
            not_done += 1
            input("What are you doing to improve this: ")
            validate = False
        elif response != "yes" or "no":
            print("invalid statement, try again")
            response = input("Enter yes or no: ")
    print("")
    report_findings(done, not_done)


def report_findings(done, not_done):
    """
    The final Results
    :param done:
    :param not_done:
    :return:
    """
    # Showing the total amount of questions answered.
    print("You answered", (done + not_done) ** 1, "Questions!")
    # Printing the end score of the completed tasks.
    print("Questions completed:", done)
    # printing the end score of the not complete tasks.
    print("Questions incomplete:", not_done)
    # Subtracting the complete with the not complete to show the final score.
    final_score = done - not_done
    print("Final Score:", final_score)

    # Using sep to help concatenate the percentage sign and the final answer
    # together for the percentage complete.
    print("Percent Complete %", done / 8 * 100, sep='')
    # Using sep to help concatenate the percentage sign and the final answer
    # together for the percentage not complete.
    print("Percent Not Complete %", not_done / 8 * 100, sep='')
    # Using floor division to help the final code to round to the
    # nearest ratio.
    if done >= 8:
        print("Everything Complete!")
        print("Great Job!")
    else:
        print("Rounded Ratio", (done / 8 * 100)
              // (not_done / 8 * 100))
    # Using Modulus to get the ratio remainder in the final code.
    if done == 8:
        print("Great Job!")
    else:
        print("Ratio Remainder", (done / 8 * 100)
              % (not_done / 8 * 100))
    # Using the end = operator to conclude the code.
    if final_score > 8:
        print("Error!")
    elif final_score == 8:
        print("Very Good!")
    elif final_score == 6:
        print("Good")
    elif final_score == 4:
        print("Satisfactory")
    elif final_score == 2:
        print("Sufficient")
    elif final_score == 0:
        print("Mediocre")
    elif final_score == -2:
        print("Need some work")
    elif final_score == -4:
        print("Bad")
    elif final_score == -6:
        print("Terrible")
    elif final_score == -8:
        print("Horrible")

    print("Assessment ", end="completed!")


if __name__ == '__main__':
    main()
