# Bikesharing Analysis and Dashboard

## Daftar Pertanyaan
- Bagaimana tren peminjaman sepeda berdasarkan bulan dari tahun 2011 - 2012?
- Apakah terdapat perbedaan pola peminjaman antara casual dan registered?
- Apakah musim berpengaruh terhadap jumlah peminjaman sepeda?
- Bagaimana pengaruh suhu, kelembaban, dan kecepatan angin terhadap jumlah peminjaman sepeda?

## Insights and Findings
- Terjadi fluktuasi yang signifikan dalam jumlah penyewa sepeda dari tahun 2011 ke tahun 2012, dengan penurunan yang tajam terutama terjadi pada akhir tahun. Namun, terdapat juga kenaikan yang signifikan pada periode tertentu, terutama dari bulan Januari hingga September 2012.
- Hal ini menunjukkan adanya variasi dalam preferensi pengguna sepeda pada bulan-bulan tertentu. Pada bulan Mei, mungkin terjadi peningkatan aktivitas rekreasi atau wisata yang menyebabkan peningkatan penggunaan sepeda tanpa pendaftaran. Sementara itu, pada bulan September, kemungkinan terdapat peningkatan penggunaan sepeda untuk tujuan transportasi sehari-hari, yang lebih sering dilakukan oleh pengguna yang terdaftar.
- Musim fall adalah musim dengan tingkat penyewaan tertinggi, sementara springer adalah musim dengan tingkat penyewaan terendah dan mengalami penurunan drastis dalam jumlah total penyewaan.
-   1. Terdapat korelasi positif antara suhu dan jumlah penyewaan sepeda, yang berarti jumlah penyewaan cenderung meningkat seiring dengan meningkatnya suhu.
    2. Korelasi antara kelembaban dan jumlah penyewaan sepeda juga positif, meskipun tidak sekuat korelasi dengan suhu. Ada penurunan jumlah penyewaan saat kelembaban rendah, menunjukkan adanya faktor lain yang memengaruhi keputusan penyewaan.
    3. Korelasi negatif antara kecepatan angin dan jumlah penyewaan sepeda, yang menunjukkan bahwa angin kencang membuat jumlah penyewaan cenderung berkurang.

## 📊 Dashboard with Streamlit
- Streamlit Cloud
- 🚧 View the dashboard on streamlit could directly on this link: [https://capital-bikeshare-alfikri.streamlit.app/](https://capital-bikeshare-alfikri.streamlit.app/) 🚧

The dashboard shows the count of total rides across the year and season. It also shows the difference casual riders and registered riders use of the bikesharing service, based on hour and day of the week.

## Run Streamlit on Local
### Install Dependencies
To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:

```bash
pip install -r requirements.txt
