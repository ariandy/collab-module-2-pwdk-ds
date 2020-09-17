# collab-module-2-pwdk-ds

### Disclaimer

Data source untuk project ini adalah hasil fetch dari [kumpulan csv pada link berikut](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).
Oleh karenanya, data yang difetch dimulai dari tanggal Feb-22 s/d Hari ini. Sementara data dari Jan-21 s/d Feb-14 yang tersedia pada [archive data](https://github.com/CSSEGISandData/COVID-19/tree/master/archived_data) tidak diikutsertakan. Ini sebabnya, ada beberapa angka yang tidak sama (entah selisih sedikit, ataupun meleset jauh) dengan yang ada pada dashboard Johns-Hopkins.

### Team
- M. Ariandy Noviar untuk task Software Engineering (SE), Documentation (DO) dan Data Wrangling (DW)
- Muhammad Firdaus Ramadhan untuk task Quality Assurance (QA), Analysis (AN), Data Visualization (VZ)

### Task
Primary:
- ![alt text](https://img.shields.io/badge/DW-Done-green.svg "Done by Ariandy") Lakukan pembagian notebook menjadi beberapa stage berdasarkan lama komputasi. Per stage, bagi menjadi beberapa step kecil dan checkpoint.
- ![alt text](https://img.shields.io/badge/SE-Done-green.svg "Done by Ariandy") Pecahkan beberapa prosedur yang kompleks (misal, data fetcher, regex matcher, dll) menjadi beberapa fungsi. Dan jadikan fungsi tersebut modular.
- ![alt text](https://img.shields.io/badge/QA-Done-green.svg "Done by Firdaus") Lakukan QA pada data. Pastikan data sudah cukup bersih untuk diproses ke tahapan selanjutnya.
- ![alt text](https://img.shields.io/badge/DW-Done-green.svg "Done by Ariandy") Buat DataFrame yang merupakan akumulasi dari kolom 'Confirmed', 'Active', 'Deaths', 'Recovered', untuk setiap negara berdasarkan datetime.now()
- ![alt text](https://img.shields.io/badge/DO-On_Going-orange.svg "On Going") Rapikan dokumentasi Jupyter dan juga GitHub
- ![alt text](https://img.shields.io/badge/AN-On_Going-orange.svg "On Going") Buat analisa tentang data yang sudah dibersihkan
- ![alt text](https://img.shields.io/badge/VZ-On_Going-orange.svg "On Going") Buat visualisasi tentang data yang sudah dibersihkan

Secondary:
- ![alt text](https://img.shields.io/badge/SE-Done-green.svg "Done by Ariandy") Backup dan maintaining Conda env.
- ![alt text](https://img.shields.io/badge/On_Going-orange.svg "On Going") Buat logging untuk setiap fungsi/proses yang cukup memakan waktu yang kurang lebihnya memerlukan 10 detik.

Tertiary (semisal masih ada waktu):
- Buat unit test untuk beberapa fungsi yang kompleks.
- Convert dataframe ke beberapa time series ('Confirmed', 'Active', 'Deaths', 'Recovered').
- Memproses [archive data](https://github.com/CSSEGISandData/COVID-19/tree/master/archived_data) agar menjadi sesuai dengan dashboard Johns-Hopkins.
- Buat dashboard sederhana.
- Membuat satu script utuh sebagai pipeline yang memproses semua data mentah menjadi sebuah dataframe yang cukup bersih untuk dianalisa.
- Improve fungsi latlong_filler_all_mean() untuk beberapa negara tertentu.
