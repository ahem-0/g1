# Function to generate permutations without repetition using recursion
def permutations_without_repetition(digits):
    # Helper function for recursion and backtracking
    def permute(current, remaining, results):
        if not remaining:  # Base case: if there are no more digits to use
            results.append(current)
        else:
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                permute(new_current, new_remaining, results)

    results = []
    permute("", digits, results)
    return results

# Function to generate permutations with repetition using nested loops
def permutations_with_repetition(digits, length):
    results = []
    # We use an iterative approach with loops to generate all possible combinations with repetition
    def generate(current):
        if len(current) == length:  # Base case: if we reach the desired length
            results.append(current)
        else:
            for digit in digits:
                generate(current + digit)

    generate("")  # Start with an empty string
    return results

# Main program to demonstrate both methods
def generate_permutations(digits, length=None, with_repetition=False):
    if with_repetition:
        # If repetition is allowed, generate permutations with repetition
        return permutations_with_repetition(digits, length)
    else:
        # If repetition is not allowed, generate permutations without repetition
        return permutations_without_repetition(digits)

# Example usage
digits = ['1', '2', '3']  # Set of digits
length = 3  # Desired length of permutations with repetition
with_repetition = True  # Flag to allow repetition

# Generate permutations based on repetition flag
perms = generate_permutations(digits, length, with_repetition)

print("Generated Permutations:")
for perm in perms:
    print(perm)
