import sympy as sp

def main():
    x = sp.Symbol('x', real=True)  # Our polynomial variable
    
    print("======================================================")
    print("Welcome to the GCD over GF(p) calculator.")
    print("Example input for polynomials:")
    print("   5x^3 + 2x^4 + x + 1   should be typed as   5*x**3 + 2*x**4 + x + 1")
    print("======================================================")
    
    while True:
        # 1) Ask for GF value
        gf_value = input("\nEnter the GF value (for GF(p)) or 'q'/'quit' to exit: ")
        if gf_value.strip().lower() in ['q', 'quit']:
            break
        
        # Validate GF(p) as an integer
        try:
            p = int(gf_value)
        except ValueError:
            print("Invalid GF value. Please enter an integer.")
            continue
        
        # 2) Ask for f(x)
        f_str = input("Please enter f(x) (or 'q'/'quit' to exit): ")
        if f_str.strip().lower() in ['q', 'quit']:
            break
        
        # 3) Ask for g(x)
        g_str = input("Please enter g(x) (or 'q'/'quit' to exit): ")
        if g_str.strip().lower() in ['q', 'quit']:
            break
        
        # 4) Parse the input strings into Sympy polynomials
        try:
            f_poly = sp.sympify(f_str, {"x": x})
            g_poly = sp.sympify(g_str, {"x": x})
        except Exception as e:
            print(f"Error parsing polynomial input: {e}")
            continue
        
        # 5) Compute GCD over GF(p)
        domain = sp.GF(p)
        gcd_poly = sp.gcd(f_poly, g_poly, domain=domain)
        
        print(f"\nThe GCD of {f_poly} and {g_poly} over GF({p}) is: {gcd_poly}")

if __name__ == "__main__":
    main()
