NUMBER_OF_PROBLEMS = 5
NUMBER_OF_DIGITS = 4

def arithmetic_arranger(problems, show_answers=False):

    operand1 = []
    operand2 = []
    operator = []
        
    #More than five problems are not allowed
    if len(problems) > NUMBER_OF_PROBLEMS:
        error1 = 'Error: Too many problems.'
        return error1

    #Split the string   
    for problem in problems:
        split_problem = problem.split(' ')
        operand1.append(split_problem[0])
        operand2.append(split_problem[2])
        operator.append(split_problem[1])

    #Checking for Correct operator
    for op in operator:
        if op != '+' and op != '-':
            error2 = "Error: Operator must be '+' or '-'."
            return error2

    #Checking whether all characters in the string are digits
    longest_operand = []
    
    for op1, op2 in zip(operand1, operand2):
        if not (op1.isdigit() and op2.isdigit()):
            error3 = 'Error: Numbers must only contain digits.'
            return error3

        #Length of operand should be less than four
        if len(op1) > NUMBER_OF_DIGITS or len(op2) > NUMBER_OF_DIGITS:
            error4 ='Error: Numbers cannot be more than four digits.'
            return error4
        #Calculating longest operand for later use
        lo = max(op1, op2, key=len)
        longest_operand.append(lo)
                                                
    #Converting string to integer values
    integer_operand1 = []
    integer_operand2 = []
    
    for first_operand, second_operand in zip(operand1, operand2):
        integer_operand1.append(int(first_operand))
        integer_operand2.append(int(second_operand))

    #Calculating answer and Appending the answer in answer[]
    answer = []

    for o, i in zip(operator, range(len(integer_operand1))):
        if o == '+':
            add = integer_operand1[i] + integer_operand2[i]
            answer.append(add)
        else:
            sub = integer_operand1[i] - integer_operand2[i]
            answer.append(sub)
        #converting integer to string
    answer = [str(a) for a in answer]
           
    #Arranging the lines       
    first_line = ''
    second_line = ''
    answers_line = ''
    dash_line = ''

    space_between_lines = 4

    for i in range(len(operand1)):
        x = len(longest_operand[i])- len(operand2[i]) + 2
        dash_line += ('-' * (len(longest_operand[i])+2))
        first_line += f'{operand1[i]:>{len(longest_operand[i])+2}}'
        second_line += f'{operator[i]:<{x}}' + operand2[i]
        
        if show_answers:
            answers_line += answer[i].rjust(len(longest_operand[i])+2)

        if i != len(operand1) - 1:
            first_line += ' ' * space_between_lines
            second_line += ' ' * space_between_lines
            dash_line += ' ' * space_between_lines
            if show_answers:
                answers_line += ' ' * space_between_lines

    arranged_lines = ''
    arranged_lines += f'{first_line.rstrip()}'
    arranged_lines += f'\n{second_line.rstrip()}'
    arranged_lines += f'\n{dash_line.rstrip()}'
    if show_answers:
        arranged_lines += f'\n{answers_line.rstrip()}'
    
    return arranged_lines


if __name__ == '__main__':
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
    print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
    print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))