from datetime import datetime
import requests
from bs4 import BeautifulSoup
from sheets import read_sheets, write_sheets
from input_lists import list_gracia_dia, list_lecturas_misa, list_textos_liturgia, list_oraciones_liturgia

date = input("Hola, registra una fecha en formato 2021-04-10: ")


def posting_sheets(list_input,sheet_name,first_cell):
    range_write=sheet_name+'!'+first_cell
    value_range={'values':list_input}
    write_sheets(range_write, value_range)

posting_sheets(list_gracia_dia(date),'Santifica el día','A22')
posting_sheets(list_lecturas_misa(date),'Santifica el día','A23')
posting_sheets(list_textos_liturgia(date),'Santifica el día','H23')
posting_sheets(list_oraciones_liturgia(date),'Santifica el día','A24')


#update_night(date,range_write):
#   update_laudes(date), update_lectio(date), update_gracia(date), update_homilia(date)
#update_morning(date,range_write):
#   update_visperas(date), update_completas(date)
