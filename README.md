# collab-module-2-pwdk-ds

### Disclaimer

Data source untuk project ini adalah hasil fetch dari [kumpulan csv pada link berikut](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).
Oleh karenanya, ada beberapa data yang terlihat anomali karena data dari [daily_reports_us](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us) tidak diikutsertakan. Ini sebabnya, ada beberapa angka (yang berhubungan dengan US) tidak sama (entah selisih sedikit, ataupun meleset jauh) dengan yang ada pada dashboard [Johns-Hopkins](https://coronavirus.jhu.edu/map.html).

### Team
- M. Ariandy Noviar untuk task Software Engineering (SE), Documentation (DOC), Data Preprocessing (DP), Software Development Engineer in Test (SDET), Data Visualization (VIZ), Dashboard (DASH)
- Muhammad Firdaus Ramadhan untuk task Data Quality Assurance (DQA), Analysis (AN), Data Visualization (VIZ)

### Task
Primary:
- ![alt text](https://img.shields.io/badge/DP-Done-green.svg "Done") Lakukan pembagian notebook menjadi beberapa stage berdasarkan lama komputasi. Per stage, bagi menjadi beberapa step kecil dan checkpoint.
- ![alt text](https://img.shields.io/badge/SE-Done-green.svg "Done") Pecahkan beberapa prosedur yang kompleks (misal, data fetcher, regex matcher, dll) menjadi beberapa fungsi. Dan jadikan fungsi tersebut modular.
- ![alt text](https://img.shields.io/badge/DQA-Done-green.svg "Done") Lakukan QA pada data. Pastikan data sudah cukup bersih untuk diproses ke tahapan selanjutnya.
- ![alt text](https://img.shields.io/badge/DP-Done-green.svg "Done") Buat DataFrame yang merupakan akumulasi dari kolom 'Confirmed', 'Active', 'Deaths', 'Recovered', untuk setiap negara berdasarkan datetime.now()
- ![alt text](https://img.shields.io/badge/DOC-Done-green.svg "Done") Rapikan dokumentasi Jupyter
- ![alt text](https://img.shields.io/badge/AN-Done-green.svg "Done") Buat analisa tentang data yang sudah dibersihkan
- ![alt text](https://img.shields.io/badge/VIZ-Done-green.svg "Done") Buat visualisasi tentang data yang sudah dibersihkan
- ![alt text](https://img.shields.io/badge/DOC-Done-green.svg "Done") Rapikan dokumentasi GitHub
- ![alt text](https://img.shields.io/badge/DASH-Done-green.svg "Done")Buat dashboard sederhana.

Secondary:
- ![alt text](https://img.shields.io/badge/SE-Done-green.svg "Done") Backup dan maintaining Conda env.
- ![alt text](https://img.shields.io/badge/SE-Done-green.svg "Done") Buat logging untuk setiap fungsi/proses yang cukup memakan waktu yang kurang lebihnya memerlukan 10 detik.
- ![alt text](https://img.shields.io/badge/SDET-Done-green.svg "Done") Buat unit test untuk beberapa fungsi yang kompleks (re.match() dan convert_a()).

Tertiary (semisal masih ada waktu):
- Convert dataframe ke beberapa time series ('Confirmed', 'Active', 'Deaths', 'Recovered').
- Memproses [daily_reports_us](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us) agar menjadi sesuai dengan dashboard Johns-Hopkins.
- Membuat satu script utuh sebagai pipeline yang memproses semua data mentah menjadi sebuah dataframe yang cukup bersih untuk dianalisa.
- Improve fungsi latlong_filler_all_mean() untuk beberapa negara tertentu.
- Menambah beberapa informasi pada dashboard.
- Improve tampilan dari dashboard (FrontEnd-side) dan juga routingnya (BackEnd-side).

### .ipynb description
- 'Stage-0.ipynb' dan 'Stage-1.ipynb' merupakan notebook yang berisi tentang step yang diperlukan untuk melakukan data cleaning.
- 'Data Processing.ipynb' adalah notebook dimana data yang telah bersih diolah menjadi data yang digunakan untuk visualisasi. 
- 'Analisa Covid.ipynb' berisi tetang analisa statistik yang didasarkan dari data yang telah diolah di 'Data Processing.ipynb'.
- 'Data Visualization.ipynb', visualisasi yang dibuat berdasarkan dari data output 'Stage-1.ipynb' dan 'Data Processing.ipynb'.

### Functions
- ariandy_stage0.py, kumpulan fungsi yang digunakan untuk 'Stage-0.ipynb'
- ariandy_stage1.py, kumpulan fungsi yang digunakan untuk 'Stage-1.ipynb'
- data_processing.py, kumpulan fungsi yang digunakan untuk 'Data Processing.ipynb'

### Unit Test
- converter_test.py, test yang diperlukan untuk menguji segala kemungkinan yang ada pada pattern Regex (re.match()) dan juga sebagai mempermudah debugging juga scaling pada convert_a()
