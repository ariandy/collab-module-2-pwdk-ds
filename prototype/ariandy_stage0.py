import os
import re
import wget
import requests
from datetime import datetime, timedelta, date

def found_or_make_directory(directory_name):
    print('Cek keberadaan direktori '+directory_name+' ...')
    if os.path.isdir(directory_name):
        print('Direktori '+directory_name+' ditemukan !')
    else:
        print('Membuat direktori '+directory_name+' ...')
        os.mkdir(directory_name)

def fetcher(url, today, x='01-22-2020'):
    print('Fetching dimulai ...')
    while x < today:
        if os.path.isfile(x+'.csv'):
            pass
        else:
            req = requests.get(url+x+'.csv')
            if req.status_code == 200:
                wget.download(url+x+'.csv', x+'.csv')
                print(' -> Sukses unduh '+x+'.csv')
            else:
                print('Pada waktu UTC, sekarang adalah pukul ' + str(datetime.utcnow())[11:16])
                print('File pada hari ini (waktu UTC) akan di upload di antara jam 04:45 dan 05:15 GMT')
        x = (datetime.strptime(x, '%m-%d-%Y') + timedelta(days=1)).strftime('%m-%d-%Y')
    print('Fetching selesai !')

def garbage_crusher(extension):
    print('Periksa keberadaan file dengan ekstensi .'+extension+' ...')
    files_in_directory = os.listdir('.')
    all_tmp = [file for file in files_in_directory if file.endswith("."+extension)]
    if len(all_tmp) == 0:
        print('Tidak ada file dengan extensi .tmp !')
    else:
        print(f'Ditemukan {len(all_tmp)} buah file dengan extensi .{extension}')
        for file in all_tmp:
            os.remove(file)
        print('Pembersihan direktori selesai !')

def pwd():
    print('Anda berada pada direktori ' + os.getcwd()[25:])
    
def today(date):
    return date.strftime('%m-%d-%Y')

def redundant_columns_synchronizer(df, column1, column2):
    df[column1] = df[column1].fillna(df[column2])
    df[column2] = df[column2].fillna(df[column1])
    if len(df[column1]) == len(df[column2]):
        print('Tersinkronisasi')
        return 1
    else:
        print('Tidak sama')

def column_eliminator(df, redundant_column, kept_column):
    if (redundant_column in df):
        if redundant_columns_synchronizer(df, redundant_column, kept_column) == 1:
            df.drop(redundant_column, axis=1, inplace=True)
            print(redundant_column+' dihapus\n')
    else:
        print(redundant_column+' sudah dihapus sebelumnya')

# Hitung banyak tanggal dengan format tertentu
# Jika ditemukan tanggal dengan format seperti X, maka nilai 'N' pada 'lu_temp' diubah ke 'Y' 
def pattern_checker(data, pattern):
    for i in range(len(data)):
        get_loc_lastUpdate = data.columns.get_loc('Last_Update')
        date_txt = data.iat[i, get_loc_lastUpdate]
        result = re.match(pattern, date_txt)
        if result != None:
            get_loc_lu_temp = data.columns.get_loc('lu_temp')
            data.iat[i, get_loc_lu_temp] = 'Y'

def pattern_checker_report(data, pattern):
    pattern_checker(data, pattern)
    print([len(data[data['lu_temp']=='Y']), len(data) == len(data[data['lu_temp']=='Y'])])

def convert_a(x):
    x = x.split(' ')
    x[0] = x[0].split('/')
    if int(x[0][0]) < 10:
        x[0][0] = '0'+x[0][0]
    else:
        pass
    if int(x[0][1]) < 10:
        x[0][1] = '0'+x[0][1]
    else:
        pass
    if int(x[0][2]) < 2000:
        x[0][2] = '20'+x[0][2]
    else:
        pass
    x[0][0], x[0][2] = x[0][2], x[0][0]
    x[0][1], x[0][2] = x[0][2], x[0][1]
    x[0] = '-'.join(x[0])
    x[1] = x[1].split(':')
    if int(x[1][0]) < 10:
        x[1][0] = '0'+x[0][1]
    else:
        pass
    x[1] = ':'.join(x[1])
    x[1] += ':00'
    return ' '.join(x)

def convert_c(x):
    return ' '.join(x.split('T'))

def higher_order_converter(df, pattern, convert_func):
    df['lu_temp'] = 'N'
    pattern_checker(df, pattern)
    x = df[df['lu_temp']=='Y'].index
    get_loc_lu = df.columns.get_loc('Last_Update')
    for i in x:
        df.iat[i, get_loc_lu] = convert_func(df.iat[i, get_loc_lu])