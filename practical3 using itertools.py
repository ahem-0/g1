import itertools
# Function to generate permutations without repetition
def permutations_without_repetition(digits):
    # Use itertools.permutations to generate permutations without repetition
    perms = itertools.permutations(digits)
    return perms
# Function to generate permutations with repetition
def permutations_with_repetition(digits, length):
    # Use itertools.product to generate permutations with repetition
    perms = itertools.product(digits, repeat=length)
    return perms
# Main program to generate permutations
def generate_permutations(digits, length=None, with_repetition=False):
    if with_repetition:
        # If repetition is allowed, use permutations with repetition
        return permutations_with_repetition(digits, length)
    else:
        # If repetition is not allowed, use permutations without repetition
        return permutations_without_repetition(digits)
# Example usage
digits = ['1', '2', '3']
length = 3  # Desired length of permutations (used for repetition)
with_repetition = True  # Set to True for repetitions, False for without repetition
# Generate and print permutations
perms = generate_permutations(digits, length, with_repetition)
print("Generated Permutations:")
for perm in perms:
    print(perm)
                                                                                    
