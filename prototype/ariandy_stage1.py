import re

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