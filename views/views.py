import streamlit as st
import pandas as pd
import sympy as sp
import controllers.methods as methods

def display_home():
    st.write("""
            **  **
            Selamat datang di Homepage metode pencarian akar. Pilih metode yang ingin digunakan pada menu di sebelah kiri.
            Website Pencarian Akar ini dibuat oleh Kelompok 6 ditujukan untuk memenuhi tugas mata kuliah Rekayasa Komputasional.
            **  **
            """)
    
    st.markdown("""
        #### Metode Pencarian Akar:
        Berikut adalah penjelasan singkat tentang metode-metode pencarian akar yang tersedia dalam aplikasi ini:
        - **Metode Bagi Dua**: Metode ini membagi interval [a, b] menjadi dua bagian yang lebih kecil secara bertahap, dengan tujuan mencari titik akar fungsi pada salah satu bagian.
        - **Metode Regula Falsi**: Metode ini menggunakan garis lurus yang menghubungkan dua titik pada grafik fungsi dan mencari akar pada titik potong garis tersebut dengan sumbu x.
        - **Metode Newton-Raphson**: Metode ini menggunakan pendekatan iteratif dengan menghitung turunan fungsi untuk mencari akar secara cepat dengan memperbaharui tebakan akar berdasarkan rumus khusus.
        - **Metode Titik Tetap**: Metode ini mencari akar fungsi dengan cara iterasi menggunakan fungsi g(x) sehingga nilai xₙ₊₁ dihitung dengan cara g(xₙ).
        - **Metode Secant**: Metode ini serupa dengan Newton-Raphson, tetapi tidak memerlukan turunan. Metode ini menggunakan dua tebakan awal untuk mencari akar fungsi.
    """
    )



def display_bisection():
    st.subheader("Metode Bagi Dua")
    st.write("Masukkan fungsi f(x), tebakan interval [a, b] dan toleransi galat.")
    
    func = st.text_input("Masukkan fungsi (dalam x):", "exp(x) - 5*x**2")
    a = st.number_input("Masukkan nilai a:", value=0.000000, format="%.6f")
    b = st.number_input("Masukkan nilai b:", value=1.000000, format="%.6f")
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.000010, format="%.6f")
    
    if st.button("Hitung"):
        # Call Bisection Method from methods.py
        hasil = methods.metode_bagi_dua(sp.sympify(func), a, b, e)
        
        # Define columns for the result table
        kolom = ["r", "a", "c", "b", "f(a)", "f(b)", "f(c)", "Selang Baru", "Lebar"]
        
        # Create a DataFrame to display the iteration results
        df = pd.DataFrame(hasil, columns=kolom)
        
        # Display the table in the app without the index column
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Calculate the estimated root based on the final iteration
        root_estimate = hasil[-1][2]  # The value of 'c' from the last iteration (estimated root)
        st.success(f"Hampiran akar x = {root_estimate:.6f}")


def display_regula_falsi():
    st.subheader("Metode Regula Falsi")
    st.write("Masukkan fungsi f(x), tebakan interval [a, b] dan toleransi galat.")
    
    func = st.text_input("Masukkan fungsi (dalam x):", "exp(x)-5*x**2")
    a = st.number_input("Masukkan nilai a:", value=0.000000, format="%.6f")
    b = st.number_input("Masukkan nilai b:", value=1.000000, format="%.6f")
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.000010, format="%.6f")
    
    if st.button("Hitung"):
        # Call Regula Falsi method from methods.py
        hasil = methods.metode_regula_falsi_perbaikan(sp.sympify(func), a, b, e)
        
        # Define columns for the result table
        kolom = ["r", "a", "c", "b", "f(a)", "f(c)", "f(b)", "Selang Baru", "Lebar"]
        
        # Create a DataFrame to display the iteration results
        df = pd.DataFrame(hasil, columns=kolom)
        
        # Center the column values for better alignment in the table
        st.dataframe(df.style.set_properties(**{'text-align': 'center'}), use_container_width=True, hide_index=True)
        
        # Calculate and display the root estimate (last value of c)
        root_estimate = hasil[-1][2]  # The last value of 'c' from the last iteration (estimated root)
        st.success(f"Hampiran akar x = {root_estimate:.6f}")


def display_titik_tetap():
    st.subheader("Metode Titik Tetap")
    st.write("Masukkan fungsi f(x) untuk referensi dan g(x) adalah fungsi iterasi dalam bentuk xₙ₊₁ = g(xₙ).")
    
    func_f = st.text_input("Masukkan fungsi f(x):", "x**2 - 2*x - 3")
    func_g = st.text_input("Masukkan fungsi g(x) (iterasi):", "(2*x + 3)**0.5")
    
    x0 = st.number_input("Masukkan tebakan awal x₀:", value=4.000000, format="%.6f")
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.000001, format="%.6f")

    hasil = st.empty()

    if st.button("Hitung"):
        # Call Fixed Point Iteration method
        hasil = methods.metode_titik_tetap(func_g, x0, e)
        
        # Create a dataframe to display iteration results
        kolom = ["r", "xr", "|xr+1 - xr|"]
        df = pd.DataFrame(hasil, columns=kolom)
        
        # Display the result as a table
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Display the final root estimate
        akar = float(hasil[-1][1])  # Last value of xr
        st.success(f"Hampiran akar x = {akar:.6f}")


def display_newton_raphson():
    st.subheader("Metode Newton-Raphson")
    st.write("Masukkan fungsi f(x), turunannya f'(x), tebakan awal x₀ dan toleransi galat.")
    
    func = st.text_input("Masukkan fungsi f(x):", "exp(x) - 5*x**2")
    derivative = st.text_input("Masukkan turunan f'(x):", "exp(x) - 10*x")
    x0 = st.number_input("Masukkan nilai x₀:", value=0.500000, format="%.6f")
    e = st.number_input("Masukkan toleransi galat:", value=0.000001, format="%.6f")

    # Button to trigger Newton-Raphson method
    if st.button("Hitung"):
        # Call the Newton-Raphson method from methods.py
        hasil = methods.metode_newton_raphson(sp.sympify(func), x0, e)

        # Define columns for the iteration result table
        kolom = ["i", "xr", "|xr+1 - xr|"]

        # Create a DataFrame to display the iteration results
        df = pd.DataFrame(hasil, columns=kolom)

        # Set index to None to hide it in the display
        df.set_index(pd.Index(range(1, len(df) + 1)), inplace=True)

        # Display the table in the app, without the index column
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Calculate and display the root estimate (last value of xr)
        root_estimate = hasil[-1][1]  # The last value of 'xr'
        st.success(f"Hampiran akar x = {root_estimate:.6f}")


def display_secant():
    st.subheader("Metode Secant")
    st.write("Masukkan fungsi f(x), tebakan awal x₀, x₁ dan toleransi galat.")
    
    # Input fields for function, initial guesses, and tolerance
    func = st.text_input("Masukkan fungsi (dalam x):", "exp(x) - 4*x**2")
    x0 = st.number_input("Masukkan nilai x₀:", value=0.500000, format="%.6f")
    x1 = st.number_input("Masukkan nilai x₁:", value=3.000000, format="%.6f")
    e = st.number_input("Masukkan toleransi kesalahan (e):", value=0.00001, format="%.6f")
    
    if st.button("Hitung"):
        # Call Secant method from methods.py
        hasil = methods.metode_secant_dengan_penanganan(sp.sympify(func), x0, x1, e)
        
        # Define the columns for the result table
        kolom = ["i", "xr", "|xr+1 - xr|"]
        
        # Create a DataFrame to display the iteration results
        df = pd.DataFrame(hasil, columns=kolom)
        
        # Display the result as a table with centered text
        st.dataframe(df.style.set_properties(**{'text-align': 'center'}), use_container_width=True, hide_index=True)
        
        # Calculate and display the root estimate (last value of xr)
        root_estimate = hasil[-1][1]  # The last value of 'xr'
        st.success(f"Hampiran akar x = {root_estimate:.6f}")
