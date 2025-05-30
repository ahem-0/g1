import math

def evaluate_polynomial(coefficients, n):
    result = 0
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        result += coef * math.pow(n, degree - i) 
    return result

# Example usage
coefficients = [4, 2, 9]  # Represents 4n^2 + 2n + 9
n = 5
result = evaluate_polynomial(coefficients, n)
print(result)
