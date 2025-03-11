#!/usr/bin/env python3

import sympy
from sympy import symbols, Poly, invert
from sympy.polys.domains import GF

def find_inverse_poly(g_expr, p_expr, field_p):
    """
    Return the inverse of the polynomial g_expr modulo p_expr in GF(field_p),
    if it exists; otherwise return None.
    """
    x = symbols('x', integer=True)
    
    # Convert expressions to Polys over GF(field_p)
    g_poly = Poly(g_expr, x, domain=GF(field_p))
    p_poly = Poly(p_expr, x, domain=GF(field_p))

    try:
        # Compute the modular inverse using the extended Euclidean algorithm
        inv_poly = invert(g_poly, p_poly, domain=GF(field_p))
        return inv_poly
    except sympy.polys.polyerrors.NotInvertible:
        return None

def main():
    x = symbols('x', integer=True)

    print("======================================================")
    print("Polynomial Inversion in GF(p)")
    print("Example input for polynomials:")
    print("   5x^3 + 2x^4 + x + 1   should be typed as   5*x**3 + 2*x**4 + x + 1")
    print("======================================================")

    while True:
        # Get the GF value
        gf_value = input("\nEnter the GF value (for GF(p)) or 'q'/'quit' to exit: ")
        if gf_value.strip().lower() in ['q', 'quit']:
            break
        
        # Validate GF(p) as an integer
        try:
            p = int(gf_value)
        except ValueError:
            print("Invalid GF value. Please enter an integer.")
            continue

        # Get the polynomial g(x)
        g_str = input("Please enter g(x) (or 'q'/'quit' to exit): ")
        if g_str.strip().lower() in ['q', 'quit']:
            break

        # Get the polynomial p(x)
        p_str = input("Please enter the modulus polynomial p(x) (or 'q'/'quit' to exit): ")
        if p_str.strip().lower() in ['q', 'quit']:
            break

        # Convert input strings into SymPy expressions
        try:
            g_poly = sympy.sympify(g_str, {"x": x})
            p_poly = sympy.sympify(p_str, {"x": x})
        except Exception as e:
            print(f"Error parsing polynomial input: {e}")
            continue

        # Compute the inverse
        inv_poly = find_inverse_poly(g_poly, p_poly, p)

        # Display result
        if inv_poly is None:
            print(f"No inverse found: {g_poly} is not invertible modulo {p_poly} in GF({p}).")
        else:
            print(f"The inverse of {g_poly} modulo {p_poly} in GF({p}) is: {inv_poly.as_expr()}")

if __name__ == "__main__":
    main()
