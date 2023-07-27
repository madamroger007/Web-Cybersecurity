def page2(st,pd,alt) :
    st.sidebar.markdown("# Sejarah Pelanggaran Data Penting")
    st.write('''
    # Sejarah pelanggaran data penting dari tahun ke tahun di AS
    Pelanggaran berskala besar yang dipublikasikan sedang meningkat, menunjukkan bahwa tidak hanya jumlah pelanggaran keamanan yang meningkat — tingkat keparahannya juga meningkat. 
    Pelanggaran data mengekspos informasi sensitif yang sering membuat pengguna yang disusupi  resiko terjadi pencurian identitas, merusak reputasi perusahaan, dan membuat perusahaan bertanggung jawab atas pelanggaran.
    ''')

    chart_data = pd.DataFrame({
        'Tahun' : [2021, 2020, 2019, 2018, 2017, 2016, 2013],
        'Jumlah Serangan' : [10, 3, 1, 1, 3, 2, 1]
    })

    bar_chart = alt.Chart(chart_data).mark_bar().encode(
        x = 'Tahun:O',
        y = 'Jumlah Serangan:Q',
    )
    st.altair_chart(bar_chart, use_container_width=True)

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    a = col1.button("2013")
    b = col2.button("2016")
    c = col3.button("2017")
    d = col4.button("2018")
    e = col5.button("2019")
    f = col6.button("2020")
    g = col7.button("2021")
    if a :
        st.info('''
        ##### 2013
        Salah satu pelanggaran terbesar sepanjang masa, yaitu tiga miliar akun Yahoo diretas pada tahun 2013.
        ''')
    elif b :
        st.info('''
        ##### 2016
        1.  Uber melaporkan bahwa hacker telah mencuri informasi dari lebih 57 juta pengendara dan pengemudi 
        2.  Uber mencoba membayar peretas untuk menghapus data curian dari 57 juta pengguna dan merahasiakan pelanggaran tersebut.
        ''')
    elif c :
        st.info('''
        ##### 2017
        1.  Peretasan Equifax Breach berakibat pada bocornya data 147.9 pelanggan, dan mengakibatkan perusahaan rugi lebih dari $4 milyar 
        2.  Lebih dari 420 juta akun pengguna situs Friendfinder’s sites dicuri
        3.  Virus Wannacry menginfeksi 100.000 grup dan lebih dari 400.000 servers di kurang lebih 150 negara, dan mengakibatkan kerugian sekitar $4 milyar
    ''')
    elif d :
        st.info('''
        ##### 2018
        Under Armour melaporkan bahwa Aplikasi “My Fitness Pal” diretas yang berimbas pada 150 juta pengguna.
        ''')
    elif e :
        st.info('''
        ##### 2019
        Peretasan data pribadi MGM mengakibatkan bocornya data dari 142 juta tamu hotel.
        ''')
    elif f :
        st.info('''
        ##### 2020
        1.  Peretasan twitter di Tahun 2020 mentargetkan 130 akun, termasuk di antaranya akun mantan presiden AS, serta akun CEO Tesla Elon Musk, yang mengakibatkan penyerang menipu $121.000 di Bitcoin melalui hampir 300 transaksi
        2.  Marriott mengungkapkan pelanggaran keamanan yang memengaruhi data lebih dari 5,2 juta tamu hotel
        3.  Penjahat dunia maya mengkloning suara direktur perusahaan U.A.E. untuk melakukan transfer bank senilai $35 juta
        ''')
    elif g :
        st.info('''
        ##### 2021
        1.  Pelanggaran data di Linkedin melibatkan 700 juta data pribadi penggunanya (93% dari anggota Linkedin)
        2.  Penyerangan data di Microsoft  berimbas ke lebih dari 30.000 organisasi di AS, termasuk di dalamnya pemerintahan dan bisnis
        3.  Terjadi pelanggaran data pribadi selama kurun waktu 2 tahun (2020-2021) ke lebih dari 533 juta pengguna internet
        4.  Haker dengan hanya mengunakan password tunggal, meretas perusahaan Colonial Pipeline dengan serangan ransomware yang menyebabkan terjadinya kekurangan bahan bakar di seluruh AS
        5.  Perusahaan pengolahan daging JBS, diserang dengan ransomware yang menyebabkan matinya sistem  pada pabrik pemrosesan daging dan unggas pada empat negeri bagian
        6.  Sekitar 48 juta orang mengalami pencurian data pribadi melalui peretasan HP
        7.  Neiman Marcus menemukan data hasil retasan berumur 18 bulan yang mengekspos data pembayaran dan informasi lain pada 4.6 juta pembeli
        8.  Data pribadi milik lebih dari 100 juta pengguna Android diretas karena salah konfigurasi dari layanan cloud.
        9.  Panasonic mengumumkan data partner bisnis, informasi pribadi kandidat pelamar pekerjaan, dan informasi dalam perusahaan telah diretas 
        10. Aplikasi trading Robinhood diretas sehingga membahayakan dati pribadi dari 5 juta pengguna
        ''')