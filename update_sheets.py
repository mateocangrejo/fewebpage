from datetime import datetime
import requests
from bs4 import BeautifulSoup
from sheets import read_sheets, write_sheets
from lecturas_misa import get_lectura_misa
from textos import get_textos_liturgia
from scrapping import get_oraciones_liturgia
from gracia_del_dia import get_gracia_dia
date = input("Hola, registra una fecha en formato 2021-04-10: ")


def post_gracia_dia(date):
    #La gracia del dia info
    list = []
    dict_gracia_dia=get_gracia_dia(date)
    list_int = []
    for k,v in  dict_gracia_dia.items():
        list_int.append(v)
    list_int.append(date)
    list.append(list_int)
    range_write='Santifica el día!A22'
    value_range={'values':list}
    write_sheets(range_write, value_range)

def post_lecturas_misa(date):
    #lecturas de la misa
    lecturas_misa_dia = get_lectura_misa(date)
    range_write='Santifica el día!A25'
    list= [["Lecturas del día","","","","",date,lecturas_misa_dia]]
    value_range={'values':list}
    write_sheets(range_write, value_range)

def post_textos_liturgia(date):
    #textos de la liturgia
    list_final = []
    dict_text_liturgia = get_textos_liturgia(date)
    dict_text_liturgia['gracia']=''
    dict_text_liturgia['homilia']=''
    order_keys = ['laudes','oficio','gracia','homilia','visperas','completas']
    order_values = list(dict_text_liturgia.get(i) for i in order_keys)
    for k,v in zip(order_keys,order_values):
        list_prov = []
        if k!='gracia' or k!='homilia':
            list_prov.append(v)
        list_final.append(list_prov)
    range_write='Santifica el día!A22'
    value_range={'values':list_final}
    write_sheets(range_write, value_range)

def post_oraciones_liturgia(date):
    #datos de las oraciones de la liturgia
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


#update_night(date,range_write):
#   update_laudes(date), update_lectio(date), update_gracia(date), update_homilia(date)
#update_morning(date,range_write):
#   update_visperas(date), update_completas(date)
