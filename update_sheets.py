from datetime import datetime
import requests
from bs4 import BeautifulSoup
from sheets import read_sheets, write_sheets
from lecturas_misa import get_lectura_misa
from textos import get_textos_liturgia
from scrapping import get_oraciones_liturgia

date = input("Hola, registra una fecha en formato 2021-04-10: ")

#lecturas de la misa

lecturas_misa_dia = get_lectura_misa(date)
range_write='Santifica el día!A25'
list= [["Lecturas del día","","","","",date,lecturas_misa_dia]]
value_range={'values':list}
write_sheets(range_write, value_range)

#textos de la liturgia
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
"""
#datos de las oraciones de la liturgia
"""
list = []
dict_oraciones_liturgia = get_oraciones_liturgia(date)
for oracion,dict_prov in  dict_oraciones_liturgia.items():
    list_int = [oracion]
    for name, item in dict_prov.items():
        #print('.................')
        #print(name)
        #print(item)
        if name=='descripcion':
            item=''
        list_int.append(item)
        #list.append(list_int)
    list_int.append(date)
    list.append(list_int)

range_write='Santifica el día!A27'
value_range={'values':list}
write_sheets(range_write, value_range)
"""

#update_night(date,range_write):
#   update_laudes(date), update_lectio(date), update_gracia(date), update_homilia(date)
#update_morning(date,range_write):
#   update_visperas(date), update_completas(date)
