def loader(st,time):
     # Tombol untuk memulai proses loading
    if st.empty():
        # Tampilkan spinner saat proses loading berlangsung
        with st.spinner("Sedang memuat..."):
            # Fungsi sleep disini hanya untuk simulasi loading
            time.sleep(5)