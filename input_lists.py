from datetime import datetime
import requests
from lecturas_misa import get_lectura_misa
from textos import get_textos_liturgia
from scrapping import get_oraciones_liturgia
from gracia_del_dia import get_gracia_dia


def list_gracia_dia(date):
    #La gracia del dia info
    list_final = []
    dict_gracia_dia=get_gracia_dia(date)
    list_int = []
    for k,v in  dict_gracia_dia.items():
        list_int.append(v)
    list_int.append(date)
    list_final.append(list_int)
    return list_final

def list_lecturas_misa(date):
    #lecturas de la misa
    lecturas_misa_dia = get_lectura_misa(date)
    range_write='Santifica el día!A25'
    list_final= [["Lecturas del día","","","","",date,lecturas_misa_dia]]
    return list_final

def list_textos_liturgia(date):
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
    return list_final

def list_oraciones_liturgia(date):
    #datos de las oraciones de la liturgia
    list_final = []
    dict_oraciones_liturgia = get_oraciones_liturgia(date)
    for oracion,dict_prov in  dict_oraciones_liturgia.items():
        #list_int = [oracion]
        list_int = []
        for name, item in dict_prov.items():
            #print('.................')
            #print(name)
            #print(item)
            if name=='descripcion':
                item=''
            list_int.append(item)
            #list.append(list_int)
        list_int.append(date)
        list_final.append(list_int)
    print(list_final)
    return list_final

def one_value_oraciones_liturgia(date, oracion):
    #datos de solo una oracion de la liturgia dada por parametro
    list_final = []
    dict_oraciones_liturgia = get_oraciones_liturgia(date)

    dict_actual_oracion=dict_oraciones_liturgia[oracion]
    list_int = []
    for name, item in dict_actual_oracion.items():
        #print('.................')
        #print(name)
        #print(item)
        if name=='descripcion':
            item=''
        list_int.append(item)
        #list.append(list_int)
    list_int.append(date)
    list_final.append(list_int)
    return list_final
