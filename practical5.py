def evaluate_polynomial(coefficients, n):
    """
    Evaluates a polynomial given its coefficients and a value of n.
    :param coefficients: List of coefficients (e.g., [9, 2, 4] for f(x) = 4x^2 + 2x + 9)
    :param n: Value of n
    :return: Result of evaluating the polynomial at n
    """
    result = 0
    for i in range(0,len(coefficients)):
        #print(coefficients[i])
        #print((n ** i))
        result += coefficients[i] * (n ** i)
        #print(result)
    return result
# Example usage
coefficients = [9, 2, 4]  # Coefficients for f(x) = 4x^2 + 2x + 9
n_value = 5
result = evaluate_polynomial(coefficients, n_value)
print(f"The value of f({n_value}) is: {result}")
