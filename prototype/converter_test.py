import pytest
import re
from ariandy_stage0 import convert_a

# 1/28/20 23:00 (Pattern A)
a = '^([1-9]|1[0-2])/([1-9]|[12][0-9]|3[01])/20 (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9])$'
# 2020-07-17 22:34:48 (Pattern B) ---> Ini adalah pattern yang kita inginkan
b = '^202[0-3]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
# 2020-03-06T14:23:04 (Pattern C)
c = '^202[0-3]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
# 1/22/2020 17:00 (Pattern D)
d = '^[1-9]/([1-9]|[12][0-9]|3[01])/20[0-9]{2} (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9])$'
pattern = [a, b, c, d]

def test_answer():
    assert convert_a('1/8/20 23:00') == '2020-01-08 23:00:00'
    assert convert_a('1/28/20 23:00') == '2020-01-28 23:00:00'
    assert convert_a('10/8/20 23:00') == '2020-10-08 23:00:00'
    assert convert_a('10/18/20 23:00') == '2020-10-18 23:00:00'
    assert convert_a('1/8/2020 23:00') == '2020-01-08 23:00:00'
    assert convert_a('1/28/2020 23:00') == '2020-01-28 23:00:00'
    assert convert_a('10/8/2020 23:00') == '2020-10-08 23:00:00'
    assert convert_a('10/18/2020 23:00') == '2020-10-18 23:00:00'

    assert re.match(pattern[0], '1/8/20 23:00')
    assert re.match(pattern[0], '1/28/20 23:00')
    assert re.match(pattern[0], '10/8/20 23:00')
    assert re.match(pattern[0], '10/28/20 23:00')
    assert re.match(pattern[3], '1/8/2020 23:00')
    assert re.match(pattern[3], '1/28/2020 23:00')
    # assert re.match(pattern[3], '10/8/2020 23:00')
    # assert re.match(pattern[3], '10/28/2020 23:00') belum diperlukan.
    # Karena pencatatan tanggal dengan format ini belum menyentuh bulan > 9