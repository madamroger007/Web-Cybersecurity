def page4(st,pd,alt) :
    st.sidebar.markdown("# Statistik Keamanan Siber selama masa COVID-19")
    st.write('''
        # Statistik Keamanan Siber selama masa COVID-19 
        COVID-19 berdampak pada setiap industri di seluruh dunia, tidak terkecuali industri yang bergerak di dunia maya. Pandemi global membuka jalan baru bagi penjahat dunia maya untuk menargetkan korban melalui kegiatan perawatan kesehatan, pengangguran, pekerjaan jarak jauh, dan banyak lagi.
        ''')
    st.write('Di bawah ini adalah beberapa statistik keamanan siber yang paling berdampak terkait dengan pandemi.')
    chart_data = pd.DataFrame({
        'Presentase  serangan (%)' : [50, 27, 238, 58, 52, 81, 50, 20],
        ' ' : [50, 27, 238, 58, 52, 81, 50, 20]
        
    })

    "Serangan selama pandemi"
    bar_chart = alt.Chart(chart_data).mark_bar().encode(
        x = 'Presentase  serangan (%):O',
        y = ' :Q',
    )
    st.altair_chart(bar_chart, use_container_width=True)
    but4 = st.button("Information")
    if but4 :
        st.info('''
        ###### 50%
        Lockdown dan metode kerja jarak jauh mengakibatkan peningkatan 50% internet traffic di seluruh dunia, yang akhirnya mengarahkan kepada peluang kejahatan baru di dunia maya.
        ''')
        st.info('''
        ###### 27%
        Serangan siber COVID-19 menargetkan bank atau organisasi layanan kesehatan.
        ''')
        st.info('''
        ###### 238%
        COVID-19 menyebabkan peningkatan serangan siber sebesar 238 persen pada bank pada tahun 2020.
        ''')
        st.info('''
        ###### 58%
        Pelanggaran data yang dikonfirmasi pada industri perawatan kesehatan meningkat sebesar 58 persen selama pandemi.        
        ''')
        st.info('''
        ###### 52%
        Legal and compliance leaders khawatir tentang risiko dunia maya pada metode pekerjaan jarak jauh yang diakibatkan oleh pihak ketiga sejak COVID-19.
        ''')
        st.info('''
        ###### 81%
        Profesional bidang keamanan siber melaporkan bahwa fungsi pekerjaan mereka berubah selama pandemi.
        ''')
        st.info('''
        ###### 50%
        Akun pengguna Zoom diretas dan dijual ke dark web  selama satu bulan pertama pada masa pandemi.
        ''')
        st.info('''
        ###### 20%
        Pekerja yang menjalankan metode jarak jauh menyebabkan pelanggaran keamanan di 20 persen organisasi selama pandemi.
        ''')