def calc_answers(solution, inp):
    if (len(solution) != len(inp)):
        print("Invalid number of answers supplied\n")
        quit()
        
    corr_count=0
    inc_count=0
    inc_list = []
    for i in range(len(inp)):
        if inp[i].upper() == solution[i].upper():
            corr_count+=1
        else:
            inc_count+=1
            inc_list.append((i+1, inp[i]))
    print("Your score is {0}/30 correct questions.\n".format(corr_count))
    print("You have {0} incorrect answers\n".format(inc_count))
    
    for tup in inc_list:
        print("Question number {0}: Correct answer = {1}, Your answer = {2}\n".format(tup[0], solution[tup[0]-1], tup[1]))
    


if __name__ == "__main__":
    solution2015 = 'DCBCACBBACAABADDCACAACDBACDBCD'
    solution2016 = 'DCAACCDCBBAABCDADCCCACDACCDBCD'
    
    paper_spec = False
    while not paper_spec:
        q_inp = input("Which paper would you like to check? (2015 or 2016): ")
        if q_inp != '2015' and q_inp != '2016':
            print("Wrong year specified")
        elif q_inp == '2015':
            solution = solution2015
            paper_spec = True
        elif q_inp == '2016':
            solution = solution2016
            paper_spec = True
            
    corr_no = False
    while not corr_no:
        inp = input("Enter multiple choice answers in a string format e.g \"ABBCDD...\" or \"abbcdd...\"\nNumber of answers must equal number of questions:")
        if (len(solution) != len(inp)):
            print("Invalid number of answers supplied\n")
        else:
            corr_no = True
            
    calc_answers(solution, inp)
    
