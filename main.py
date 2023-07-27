import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import time
import app

def mainpage():
    app.main_page(st,Image)
    

def Halamankedua():
    app.page2(st,pd,alt)
    

def Halamanketiga():
    app.page3(st,pd,alt)
    

def Halamankeempat():
    app.page4(st,pd,alt)
    

page_names = {
    "Halaman Utama" : mainpage,
    "Sejarah Pelanggaran Data Penting" : Halamankedua,
    "Statistik Kejahatan Siber Berdasarkan Tipe Serangan" : Halamanketiga,
    "Statistik Keamanan Siber selama masa COVID-19" : Halamankeempat,
}


option = st.sidebar.selectbox("Pilih Halaman", page_names.keys())

def main() -> page_names:
   app.loader(st,time)
   page_names[option]()
   app.Sidebar(st,time)
   

if __name__ == "__main__":
    main()



