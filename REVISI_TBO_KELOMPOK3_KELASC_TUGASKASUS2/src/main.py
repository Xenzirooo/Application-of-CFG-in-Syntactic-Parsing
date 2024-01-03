import streamlit as st
import re
from modules.cyk_algorithm import is_accepted, get_table_element
from modules.cnf_algorithm import get_set_of_production, print_result_to_file

def main():
    st.title("Indonesian sentence Parsing using CYK Algorithm")
    kalimat = st.text_input("Masukkan Kalimat:")

    # Mengecek apakah tombol "Cek Sekarang!" ditekan
    if st.button("Cek Validalitas Struktur"):
        if not kalimat:
            st.warning("Kalimat Kosong.")
        else:
            semua_alphabet = get_set_of_production()
            semua_kata = [val for key, value in semua_alphabet.items() if key not in ["K", "S", "P", "O", "Pel", "Ket", "NP", "VP", "AdjP", "PP"] for val in value]

            cek_kalimat = re.sub(r'\s+', ' ', kalimat).strip()
            cek_kata = cek_kalimat.split()
            kata_tidak_ketemu = [kata for kata in cek_kata if kata not in semua_kata]

            if kata_tidak_ketemu:
                kata_tidak_ketemu_str = ', '.join(kata_tidak_ketemu)
                st.error(f"Kata-kata tidak ditemukan: {kata_tidak_ketemu_str}")
            elif is_accepted(cek_kalimat):
                st.success("Kalimat tersebut valid dan sesuai Grammar Indonesia.")
                st.subheader("Konstruksi Triangular Table:")
                triangular_table = get_table_element(cek_kalimat)
                st.table(triangular_table)
            else:
                st.error("Kalimat tersebut Tidak valid.")
                st.subheader("Konstruksi Triangular Table:")
                triangular_table = get_table_element(cek_kalimat)
                st.table(triangular_table)

if __name__ == "__main__":
    main()
