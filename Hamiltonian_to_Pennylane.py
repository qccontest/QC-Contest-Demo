import re
def parse_hamiltonian_string(hamiltonian_str):
    """
    Parse the input Hamiltonian string into a list of tuples.
    """
    term_pattern = re.compile(r'([\+\-]?\s{0,}\d+\.\d+)\s*\*\s*([IXYZ]+)')
    terms = term_pattern.findall(hamiltonian_str)
    
    parsed_terms = [(term[1], float(term[0].replace(" ", ""))) for term in terms]
    return parsed_terms

def convert_to_pennylane_format(term_str, coefficient):
    """
    Convert a term from the parsed format to PennyLane's Hamiltonian format.
    """
    operators = list(term_str)
    terms = []
    for i, op in enumerate(operators):
        if op != 'I':
            terms.append(f"{op}{i}")
    term_in_pennylane = ' '.join(terms)
    if not term_in_pennylane:
        term_in_pennylane = "I0"  # This ensures we're correctly representing identity terms
    return f"({coefficient}) [{term_in_pennylane}]"

# Input Hamiltonian string
input_str = """
-51.1139071673799 * IIIIIIIIIIII
+ 12.41620827390893 * IIIIIIIIIIIZ
+ 0.12057948842535543 * IIIIIIIIIIYY
+ 0.12057948842535543 * IIIIIIIIIIXX
+ 0.0327578387990602 * IIIIIIIIIYZY
+ 0.0327578387990602 * IIIIIIIIIXZX
"""

# Parse the Hamiltonian
parsed_hamiltonian = parse_hamiltonian_string(input_str)

# Convert to PennyLane format
converted_hamiltonian = []
for term_str, coeff in parsed_hamiltonian:
    converted_term = convert_to_pennylane_format(term_str, coeff)
    converted_hamiltonian.append(converted_term)

# Join the terms with '+' to get the final Hamiltonian
final_hamiltonian = '\n+ '.join(converted_hamiltonian)
print(final_hamiltonian)
