import numpy as np
import sympy as sp

# Definisikan simbol
x = sp.symbols('x')

# Fungsi evaluasi nilai
def f_val(f, val):
    return float(f.subs(x, val))

# Metode Bagi Dua
def metode_bagi_dua(f, a, b, E):
    data = []
    iteration = 0  # Start the iteration counter at 0
    while True:
        c = (a + b) / 2  # Calculate the midpoint
        fa, fb, fc = f_val(f, a), f_val(f, b), f_val(f, c)

        # Determine the new interval based on the sign of the function values
        if fa * fc > 0:
            selang_baru = 'c, b'
            lebar = b - c
        else:
            selang_baru = 'a, c'
            lebar = c - a

        # Append the iteration results, including 'r'
        data.append([iteration, a, c, b, fa, fb, fc, selang_baru, lebar])

        # Update the interval [a, b]
        a, b = (c, b) if fa * fc > 0 else (a, c)

        # Break the loop if the width of the interval is less than the tolerance
        if lebar < E:
            break
        
        iteration += 1  # Increment the iteration number
    
    return data



def metode_regula_falsi_perbaikan(f, a, b, E):
    data = []
    FA, FB = f_val(f, a), f_val(f, b)
    iteration = 0  # Iteration counter
    while True:
        # Calculate c using Regula Falsi formula
        c = b - (FB * (b - a) / (FB - FA))
        FC = f_val(f, c)

        # Logic to adjust a and b based on function values
        if abs(FC) < 1e-8:  # If f(c) is sufficiently close to zero, it's the root
            a = c
            b = c
        elif f_val(f, a) * FC < 0:
            b = c  # Update the interval to [a, c]
        else:
            a = c  # Update the interval to [c, b]

        # Calculate the width of the interval
        lebar = abs(b - a)

        # Determine the new interval based on function values
        if f_val(f, a) * f_val(f, c) > 0:
            selang_baru = "c, b"
        else:
            selang_baru = "a, c"

        # Append the result of each iteration
        data.append([iteration, a, c, b, FA, FC, FB, selang_baru, lebar])

        # Stop if the width is within the tolerance or the function value at c is sufficiently close to zero
        if lebar < E:  # Adjust tolerance for stricter precision
            break

        iteration += 1

    return data





# Metode Newton-Raphson
def metode_newton_raphson(f, x0, E):
    df = sp.diff(f, x)  # Calculate the derivative of the function
    data = []
    i = 0
    Nmaks = 30  # Maximum iterations
    while i < Nmaks:
        fx = f_val(f, x0)  # Evaluate f(xₙ)
        dfx = f_val(df, x0)  # Evaluate f'(xₙ)
        
        # Check for division by zero
        if abs(dfx) < 1e-9:
            return data, "Pembagian dengan bilangan yang hampir nol"
        
        # Update x using the Newton-Raphson formula
        x1 = x0 - fx / dfx
        galat = abs(x1 - x0)  # Calculate the error |xₙ₊₁ - xₙ|
        
        # Handle first iteration error (set to '.')
        error_display = '.' if i == 0 else f"{galat:.6f}"
        
        # Append the iteration results
        data.append([i, x0, error_display])  # Store error display as string
        
        # Stop if the error is within the tolerance
        if galat < E:
            break
        
        # Update xₙ for the next iteration
        x0 = x1
        i += 1
    
    return data





# Metode Titik Tetap
def metode_titik_tetap(g_str, x0, E=1e-6, Nmax=30):
    g = sp.sympify(g_str)
    data = []
    for r in range(Nmax):
        # Calculate the next iteration of x
        xr = f_val(g, x0)
        
        # Calculate the error (|xr+1 - xr|)
        galat = abs(xr - x0)
        
        # Append the iteration results
        data.append([r, xr, galat])
        
        # Check if the error is within the tolerance
        if galat < E:
            break
        
        # Update the current value of x
        x0 = xr
    
    return data


# Define function f(x)
def f_val(f, val):
    return float(f.subs(x, val))

# Metode Secant
def metode_secant_dengan_penanganan(f, x0, x1, epsilon1=1e-6, epsilon2=1e-9, Nmaks=30):
    data = []
    i = 0  # Start from iteration 0
    while i < Nmaks:
        f0 = f_val(f, x0)  # Calculate f(x0)
        f1 = f_val(f, x1)  # Calculate f(x1)

        # Avoid division by a very small number
        if abs(f1 - f0) < epsilon2:
            return data, "Pembagian dengan bilangan yang hampir nol"
        
        # Secant formula to calculate the next approximation x2
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        galat = abs(x2 - x1)  # The error is the difference between x2 and x1

        # Append the iteration results with the current iteration index, x2, and error
        data.append([i, x2, galat])

        # Stop if the error is within the tolerance
        if galat < epsilon1:
            break

        # Update x0 and x1 for the next iteration
        x0, x1 = x1, x2
        i += 1

    return data





