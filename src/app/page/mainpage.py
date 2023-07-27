import app

def main_page(st, Image):
    st.sidebar.markdown("# Halaman Utama ")
    image = Image.open('src/image/cyberattack.png')
    st.title('Cyber Security')
    st.title('\n\n')
    st.image(image, output_format="PNG")
    st.write('\n\n')
    st.write('''
    Keamanan siber adalah operasi sehari-hari bagi banyak bisnis.
    Peretasan data biasanya akibat dari perlindungan data yang kurang, efek samping dari pandemi global, dan peningkatan pemanfaatan tekologi canggih. Pembobolan seringkali berasal dari sumber yang umum digunakan di tempat kerja seperti telepon seluler dan perangkat IoT (internet of things). Selain itu, COVID-19 telah meningkatkan terjadinya serangan siber dikarenakan diberlakukannya metode bekerja di rumah (WFH = Work From Home). Pekerjaan jarak jauh terus menjadi fokus bagi banyak perusahaan besar, menyebabkan operasi berbasis cloud berkembang luas. Memperluas jaringan 5G perangkat yang terhubung dengan kecepatan lebih cepat dan bandwidth lebih besar.
    Penelitian keamanan baru-baru ini menunjukkan bahwa sebagian besar perusahaan memiliki keamanan siber yang buruk, yang membuat mereka rentan terhadap kehilangan data. Adalah sangat penting bagi perusahaan untuk meningkatkan kesadaran mengenai keamanan siber, pencegahan, dan praktik terbaik keamanan, sehingga menjadi bagian dari budaya mereka.
    ''')
   
    video_file = open('src/image/Cybersecurity.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    app.footercapt(st)
    
