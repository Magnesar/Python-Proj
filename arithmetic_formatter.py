def arithmetic_arranger(problems, show_answers=False):
    Max_prob = 5
    operators = []
    if len(problems)>5:
        err = 'Error: Too many problems.'
        return err
    else:
        upper = []
        lower = []  
        for problem in problems:
            problem = problem.replace(" ", "")
            #print(problem)
            for char in problem:
                if char.isdigit() == False:
                    i = problem.index(char)
                    upper.append(problem[:i])
                    operators.append(char)
                    lower.append(problem[i+1:])
        
        for operator in operators:
            i = operators.index(operator)
            if operator != '+' and operator != '-':
                err = "Error: Operator must be '+' or '-'."
                return err
            elif len(upper[i])>4 or len(lower[i])>4:
                err = 'Error: Numbers cannot be more than four digits.'
                return err
            elif upper[i].isdigit() == False or lower[i].isdigit() == False:
                err = 'Error: Numbers must only contain digits.'
                return err
    
        #Now to printing since no errors were found
        arranged_problem = ''
        upper_layer = ''
        lower_layer = ''
        dashes = ''
        solutions = ''
        space = ' '*4
        for i in range(len(upper)):
            #dashes
            dash = '--' + '-'*max(len(upper[i]),len(lower[i]))  
            #new upper layer

            un = ' '*(len(dash)-len(upper[i])) + upper[i]

            #new lower layer
            ln = operators[i] + ' '*(len(dash)-len(lower[i])-1) + lower[i] 

            #sol
            if operators[i] == '+':
                sol = str(int(upper[i]) + int(lower[i]))
            else:
                sol = str(int(upper[i]) - int(lower[i]))
            
            #Creating the complete layers
            if i != len(upper)-1:
                dashes += dash + " "*4
                upper_layer += un +" "*4
                lower_layer += ln + " "*4
                solutions +=  " "*(len(dash)-len(sol))+ sol + " "*4
            else:
                dashes += dash
                upper_layer += un
                lower_layer += ln 
                solutions +=  " "*(len(dash)-len(sol))+ sol


           
            
            


            
            
            
        if show_answers == True:
            arranged_problem = upper_layer+ '\n' +lower_layer + '\n' + dashes + '\n' + solutions
        else:
            arranged_problem = upper_layer+ '\n' +lower_layer + '\n' + dashes
        return arranged_problem

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))

