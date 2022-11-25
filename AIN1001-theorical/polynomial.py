

def parse_polynomial(polynomial_string):
    components = polynomial_string.split(" ")
    length = len(components)
    if length % 2 == 1:
        return None
    polynomial_list = []
    for i in range(0, length, 2):
        
        polynomial_list.append(tuple([components[i], components[i+1]]))
        
        # The loop for parsing polynomial values
        
    return polynomial_list


def compute_polynomial(p, x_value):
    y_value = 0.0
    for component in p:
        
        y_value += (float(component[1]) * (x_value ** round(float(component[0]))))
        
        # The computing loop with the given variables and exponents
    return y_value


def print_polynomial(p):
    for component in p:
        print(f"{component[0]:>12}", end="")
    print()
    for component in p:
        print(f"{component[1]:9.2f} x ", end="")
    print()


polynomial = None
while polynomial is None:
    user_input = input("Enter exponents and coefficients: ")
    polynomial = parse_polynomial(user_input)
print_polynomial(polynomial)
print(polynomial)

while True:
    user_input = input("Enter x value: ")
    if user_input == "quit":   # Condition for leaving the loop
        break
    x = float(user_input)
    y = compute_polynomial(polynomial, x)  # Call to the function
    print(f"The value of the polynomial at {x} is {y:12.4f}")