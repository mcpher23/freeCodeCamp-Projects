import re


# Defining the function to perform the formatting
def solver(problems, result=False):

    # Creating empty variables that will take on the roles of the problems later
    top = ""
    bottom = ""
    dashes = ""
    sums = ""

    # Loop through the list of problems
    for problem in problems:
        
        # Perform searches using the re library to match characters in the string and check the problem conditions. Here the [^] operand allows us to search for "if not one of these"
        if re.search("[^+-/*0-9\s]", problem):
            return("Error: Numbers must only contain digits.")
        
        elif re.search("[/*]", problem):
            return("Error: Operator must be '+' or '-'.")
        
        elif len(problems) > 5:
            return("Error: Too many problems.")
        
        # Split the problem into three sections to allow us to peform the formatting        
        digits1 = problem.split()[0]
        operator = problem.split()[1]
        digits2 = problem.split()[2]
        
        # Find the length of the longest number in the problem
        length = max(len(digits1), len(digits2))
        
        if length >= 5:
            return("Error: Numbers cannot be more than four digits.")
        
        if operator == "+":
            sum = int(digits1) + int(digits2)
                
        elif operator == "-":
            sum = int(digits1) - int(digits2)
        
        # The formating here is done using the r.just method and the input is using the length and the extra 2 spaces
        digits1 = digits1.rjust(length + 2)
        digits2 = digits2.rjust(length + 1)
        dash = "-" * (length + 2)
        sum = (str(sum)).rjust(length + 2)
        
        # This section makes sure that the 4 spaces inbetween the problems is not replicated after the last problem set
        if problem != problems[-1]:
            top += digits1 + "    "
            bottom += (operator + digits2) + "    "
            dashes += dash + "    "
            sums += sum + "    "
            
        else:
            top += digits1
            bottom += (operator + digits2)
            dashes += dash
            sums += sum
    
    # Here we check for the optional boolean input that will add the result of the problem if found to be True   
    if result == False:
        arranged_problems = top + "\n" + bottom + "\n" + dashes
            
    elif result == True:
        arranged_problems = top + "\n" + bottom + "\n" + dashes + "\n"  + sums     
      
    return(arranged_problems)


# Test Case
problems = ['3801 - 2', '123 + 49']

output = solver(problems, True)

print(output)

# Expected Result
#  3801      123
#-    2    +  49
#------    -----
#  3799      172