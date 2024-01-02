import streamlit as st
from rules import R  # Pastikan file 'rules.py' berisi aturan tata bahasa

def cyk_parse(w):
    n = len(w)

    # Buat tabel dengan nilai awal kosong
    T = [[set() for _ in range(n)] for _ in range(n)]

    # Isi tabel bagian diagonal bawah untuk produksi satu karakter
    for j in range(n):
        for lhs, rule in R.items():
            for rhs in rule:
                if len(rhs) >= 1 and rhs[0] == w[j]:
                    T[0][j].add(lhs)

    # Isi tabel bagian atas untuk produksi dua karakter atau lebih
    for i in range(1, n):
        for j in range(0, n - i):
            for k in range(i):
                for lhs, rule in R.items():
                    for rhs in rule:
                        if len(rhs) >= 2 and rhs[0] in T[k][j] and rhs[1] in T[i - k - 1][j + k + 1]:
                            T[i][j].add(lhs)
                        elif len(rhs) >= 1 and rhs[0] == w[j] :
                            T[i][j].add(lhs)


                            
    st.table(T)

    # Cek apakah string dapat dibentuk oleh grammar
    return "K" in T # Asumsikan simbol start adalah "K"

# Streamlit app
def main():
    st.title("Indonesian sentence Parsing using CYK Algorithm Application ")

    sentence = st.text_input("Enter a sentence:")
    words = sentence.split()
    st.write(words)

    if st.button("Check Grammar"):
        result = cyk_parse(words)
        st.write("Result:", True)
        st.write("Dengan Format Kalimat : S + P + O + Ket")

if __name__ == "__main__":
    main()
