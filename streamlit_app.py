import streamlit as st

st.title("❤️Welcome To The SKZ Hot MEGAVERSE Web 👀🖤")
st.write("this web is made by a stay, HII Im Mallika from XF and leeknow is my bias")



st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
   st.write(f"{angka} adalah Bilangan Genap")
else:
   st.write(f"{angka} adalah Bilangan Ganjil")
