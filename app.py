import streamlit as st
import views.views as views

# Cek apakah halaman pertama kali dibuka menggunakan session_state
if 'first_load' not in st.session_state:
    st.session_state.first_load = True  # Set status pertama kali dibuka

st.set_page_config(
    page_title="Metode Pencarian Akar",
    page_icon="assets/page-icon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar untuk memilih metode
with st.sidebar:
    st.title("Menu")
    
    # Tombol Homepage dan About Us dengan ukuran yang sama dan sejajar
    col1, col2 = st.columns([1, 1])  # Membuat dua kolom yang memiliki ukuran yang sama
    
    with col1:
        homepage_clicked = st.button("Homepage", icon="🏠")
    
    with col2:
        about_us_clicked = st.button("About Us", icon="ℹ️")
    
    # Pilih Metode hanya jika Homepage atau About Us tidak diklik
    SELECTION = st.selectbox(
        "Pilih Metode",
        ("Pilih Metode", "Bagi Dua", "Regula Falsi", "Iterasi Titik Tetap", "Newton Raphson", "Secant"),
        index=0
    )

# Menampilkan Homepage jika pertama kali dibuka atau jika tombol Homepage ditekan
if st.session_state.first_load or homepage_clicked:
    st.session_state.first_load = False  # Set first_load ke False setelah pertama kali
    st.title("Homepage")
    views.display_home()  # Tampilkan konten Homepage

# Menampilkan halaman About Us jika tombol About Us ditekan
elif about_us_clicked:
    st.title("About Us")
    st.write("""
        **  **
        **Kelompok 6 - 3IA12 - Rekayasa Komputasional**

        Kami adalah kelompok yang terdiri dari beberapa mahasiswa yang berkolaborasi untuk menyelesaikan tugas mata kuliah Rekayasa Komputasional. 
        **  **
        
        **Anggota Kelompok:**
        1. Annisa Amirah Abdillah (50422233)
        2. Katharina Stasiama Sarto (50422769)
        3. Muhammad Afwan Sudiro (50422973)
        4. Muhammad Aidil Kusumayadi (50422974)
        5. Raihan Musyaffa Hanif (51422357)
        **  **

        **Tujuan Proyek:**
        Proyek ini bertujuan untuk membangun aplikasi berbasis web yang dapat membantu pengguna dalam menyelesaikan masalah pencarian akar fungsi dengan menggunakan berbagai metode numerik yang telah dipelajari dalam mata kuliah.
    """)

# Menampilkan pilihan metode setelah Homepage atau About Us
else:
    if SELECTION == "Pilih Metode":
        st.sidebar.markdown("### Silakan Pilih Metode di atas")

    elif SELECTION == "Bagi Dua":
        views.display_bisection()
    elif SELECTION == "Regula Falsi":
        views.display_regula_falsi()
    elif SELECTION == "Iterasi Titik Tetap":
        views.display_titik_tetap()
    elif SELECTION == "Newton Raphson":
        views.display_newton_raphson()
    elif SELECTION == "Secant":
        views.display_secant()
