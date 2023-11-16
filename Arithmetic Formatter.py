def arithmetic_arranger(problems, include_result = False):
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = ["+", "-"]
    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for value in problems:
        operation = value.split(" ")

        if operation[1] not in operators:
            return "Error: Operator must be '+' or '-'."

        operand_1 = operation[0]
        operand_2 = operation[2]

        if operand_1.isdigit() == False or operand_2.isdigit() == False :
            return "Error: Numbers must only contain digits."

        if len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_spaces_to_fill = max(len(x) for x in operation)
        dash = "-"
        space = " "

        line1.append(operand_1.rjust(max_spaces_to_fill+2)+ space*4)
        line2.append(operation[1] + space + operand_2.rjust(max_spaces_to_fill)+space*4)
        line3.append(dash * (max_spaces_to_fill+2)+space*4)
        result = (str(eval(value)))
        line4.append(result.rjust(max_spaces_to_fill+2)+space*4)

    line1= ''.join(map(str, line1))
    line1= line1.rstrip()
    line2 = ''.join(map(str, line2))
    line2= line2.rstrip()
    line3 = ''.join(map(str, line3))
    line3= line3.rstrip()
    line4 = ''.join(map(str, line4))
    line4= line4.rstrip()
    if include_result == True:
        arranged_problems = line1 + "\n" + line2 + "\n"+ line3+ "\n"+ line4
    if include_result == False:
        arranged_problems = line1 + "\n" + line2 + "\n"+ line3
    print(arranged_problems)
    return arranged_problems

arithmetic_arranger( ["3801 - 2", "123 + 49"], True)
