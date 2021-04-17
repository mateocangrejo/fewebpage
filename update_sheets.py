from datetime import datetime
import requests
from bs4 import BeautifulSoup
from sheets import read_sheets, write_sheets
from lecturas_misa import get_lectura_misa
from textos import get_textos_liturgia

date = input("Hola, registra una fecha en formato 2021-04-10: ")

"""
lecutars_misa_dia = get_lectura_misa(date)

range_write='Santifica el día!A22'
list= [[date,lecutars_misa_dia]]
value_range={'values':list}
write_sheets(range_write, value_range)
"""
list = []
dict_text_liturgia = get_textos_liturgia(date)
for k,v in  dict_text_liturgia.items():
    list_int = [date,k,v]
    list.append(list_int)
    #print(k)
    #print('.................')
    #print(v)
range_write='Santifica el día!A22'
value_range={'values':list}
write_sheets(range_write, value_range)
