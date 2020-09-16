# collab-module-2-pwdk-ds

### Disclaimer

Data Source ini adalah hasil fetch dari [kumpulan csv pada link berikut](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).
Oleh karenanya, data yang difetch dimulai dari tanggal Feb-22 s/d Hari ini. Sementara data dari Jan-21 s/d Feb-14 yang tersedia pada [archive data](https://github.com/CSSEGISandData/COVID-19/tree/master/archived_data) tidak diikut sertakan. Ini sebabnya, ada beberapa angka yang tidak sama (entah kurang lebih, ataupun meleset jauh) dengan yang ada pada dashboard Johns-Hopkins.

Partner : Firdaus

Primary Task:
- Lakukan pembagian notebook menjadi beberapa stage berdasarkan lama komputasi. Per stage, bagi menjadi beberapa step kecil dan checkpoint. ![alt text](https://img.shields.io/badge/Ariandy-Done-green.svg "Done by Ariandy")
- Pecahkan beberapa prosedur yang kompleks (misal, data fetcher, regex matcher, dll) menjadi beberapa fungsi. Danjadikan fungsi tersebut modular. ![alt text](https://img.shields.io/badge/Ariandy-Done-green.svg "Done by Ariandy")
- Lakukan QA pada data. Pastikan data sudah cukup bersih untuk diproses ke tahapan selanjutnya. ![alt text](https://img.shields.io/badge/Firdaus-Done-green.svg "Done by Firdaus")
- Rapikan dokumentasi Jupyter dan juga GitHub ![alt text](https://img.shields.io/badge/On_Going-orange.svg "On Going")
- Buat analisa dan visualisasi tentang data yang sudah dibersihkan ![alt text](https://img.shields.io/badge/On_Going-orange.svg "On Going")

Secondary Task:
- Backup dan maintaining Conda env. ![alt text](https://img.shields.io/badge/Ariandy-Done-green.svg "Done by Ariandy")
- Buat logging process untuk setiap process yang cukup memakan waktu yang kurang lebihnya memerlukan 10 detik. ![alt text](https://img.shields.io/badge/Ariandy-Done-green.svg "Done by Ariandy")

Extra Task (semisal masih ada waktu):
- Buat unit test untuk beberapa fungsi yang kompleks.
- Convert dataframe ke time series
- Memproses [archive data](https://github.com/CSSEGISandData/COVID-19/tree/master/archived_data) agar menjadi sesuai dengan dashboard Johns-Hopkins.
- Buat dashboard sederhana.
- Membuat satu script utuh sebagai pipeline yang meproses semua data mentah menjadi sebuah dataframe yang cukup bersih untuk dianalisa.
