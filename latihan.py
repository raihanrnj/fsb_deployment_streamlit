import streamlit as st

st.title("Contoh Program sederhana")

bil1 = st.number_input("Masukkan angka Pertama")
bil2 = st.number_input("Masukkan angka Kedua")

hitung = st.button("Hitung")

if hitung:
    total = bil1 + bil2
    st.success(f"Hasil penjumlahan adalah : {total}")
    st.balloons()
