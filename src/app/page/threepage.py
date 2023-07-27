def page3(st, pd, alt):
    st.sidebar.markdown("# Statistik Kejahatan Siber Berdasarkan Tipe Serangan")
    st.write(
        """
        # Statistik Kejahatan Siber Berdasarkan Tipe Serangan
        Masalah keamanan siber beragam dan selalu berkembang. Malware serta virus baru ditemukan setiap hari. Sangat penting untuk memahami jenis serangan yang paling umum dan dari mana asalnya untuk menjaga dari penyusupan di masa depan.
        Beberapa serangan yang paling umum termasuk phishing, whaling, malware, social engineering, ransomware, dan serangan distributed denial of service (DDoS).
        """
    )
    st.write(
        "Baca selengkapnya di bawah ini untuk memahami serangan siber yang paling umum."
    )
    "1. Ransomware dan Malware"
    st.subheader("Ransomware dan Malware")
    chart_data = pd.DataFrame(
        {
            "Presentase  serangan (%)": [518, 358, 435, 26, 112, 94, 8, 48],
            " ": ["a", "b", "c", "d", "e", "f", "g", "h"],
        }
    )

    bar_chart = (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(
            y="Presentase  serangan (%):Q",
            x=" :O",
        )
    )
    st.altair_chart(bar_chart, use_container_width=True)
    but1 = st.button("Ransomware dan Malware")
    if but1:
        st.warning("Information Ransome and Malware", icon="⚠️")
        st.write(
            """Tebusan untuk ransomeware meningkat pesat sebesar 518% di 2021 menjadi $570.000, Malware meningkat 385% di 2020, Ransomware meningkat 435% di 2020, Sekitar 26% dari keseluruhan trafik web berupa bad bot traffic, Dokumen MS Word merupakan target yang paling banyak, dengan serangan meningkat 112%, Sebesar 94% malware disebarkan melalui email, Hanya 8% bisnis yang membayar tebusan yang diminta hacker menerima data mereka kembali,48% lampiran dari email berbahaya, merupakan file MS Office"""
        )

    st.title("\n\n\n")
    "2. Phising"
    st.subheader("Phising")
    chart_data = pd.DataFrame(
        {"Presentase  serangan (%)": [57, 65, 80], " ": [1, 2, 3]}
    )

    bar_chart = (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(
            y="Presentase  serangan (%):Q",
            x=" :O",
        )
    )
    st.altair_chart(bar_chart, use_container_width=True)

    but2 = st.button("Phising")
    if but2:
        st.warning("Information Phising", icon="⚠️")
        st.write(
            """ 
Sebanyak 57% organisasi terkena phising secara harian dan mingguan, Sebesar 65% grup kejahatan siber menggunakan spear-phising sebagai vektor infeksi utama, Serangan phishing menyumbang lebih dari 80 persen insiden keamanan dari yang dilaporkan
"""
        )
    st.title("\n\n\n")

    "3. Serangan IoT, DDoS"
    st.subheader("Serangan IoT, DDoS")
    chart_data = pd.DataFrame(
        {"Presentase  serangan (%)": [30, 90, 60], " ": [1, 2, 3]}
    )

    bar_chart = (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(
            y="Presentase  serangan (%):Q",
            x=" :O",
        )
    )
    st.altair_chart(bar_chart, use_container_width=True)

    but3 = st.button("IoT, DDoS")
    if but3:
        st.warning("Information IoT, DDoS", icon="⚠️")
        st.write(
            """
                    Pelanggaran data melibatkan pelaku internal,
                    Serangan eksekusi kode jarak jauh terkait dengan cryptomining,
                    Organisasi percaya antivirus perangkat lunak mereka tidak berguna melawan ancaman dunia maya saat ini,
"""
        )
    st.title("\n\n\n")
