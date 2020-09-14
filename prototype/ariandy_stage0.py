import os
import wget
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
            wget.download(url+x+'.csv', x+'.csv')
            print(' -> Sukses unduh '+x+'.csv')
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