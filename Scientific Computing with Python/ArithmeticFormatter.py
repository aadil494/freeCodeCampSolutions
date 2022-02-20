
def formater(problems,answer=False): 
    first_line = ""
    second_line = ""
    third_line = ""
    solution = ""
    if len(problems) > 5:
            return "Error: Too many problems"
    for problem in problems:
        terms = problem.split(" ")
        if len(terms) != 3:
            return "Error: Invalid problem"
        if terms[1] not in ["+","-"]:
            return "Error: Operator must be '+' or '-'"
        if not (terms[0].isdecimal() and terms[2].isdecimal()):
            return "Error: Numbers must only contain digits." 
        if len(terms[0]) > 4 or len(terms[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        max_places = max([len(i) for i in terms])
        first_line += f"{(max_places- len(terms[0]) +2 ) * ' ' if len(terms[0]) < max_places else 2*' ' }{terms[0]}\t"
        second_line += f"{terms[1] + (max_places- len(terms[2]) +1 ) * ' ' if len(terms[2]) < max_places else terms[1] +1*' ' }{terms[2]}\t"
        third_line += (max_places +2) * '-' + '\t'
        if(answer == True):
            ans = str(eval(problem))
            solution += f"{(max_places - len(ans) + 2)*' '}{ans}\t"
    if answer:
        return f"{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}\n{solution.rstrip()}"
    return first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip() + "\n"

