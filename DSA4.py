def find_solutions(n, C):
    solutions = []

    def find_combination(curr, start, remaining):
        
        if len(curr) == n:
            if remaining == 0:
                solutions.append(curr.copy())  
            return
        
        
        for i in range(start, C + 1):
            if remaining - i >= 0:  
                curr.append(i)  
                find_combination(curr, i, remaining - i)  
                curr.pop()  

    find_combination([], 0, C)
    
    return solutions

n = 3
C = 5
solutions = find_solutions(n, C)
print(solutions)
