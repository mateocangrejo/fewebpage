from datetime import datetime,timedelta
import requests
import pytz
from bs4 import BeautifulSoup
from sheets import read_sheets, write_sheets
from input_lists import *
from whatsapp import send_whatsapp_message

co_tz = pytz.timezone('America/Bogota')
now = datetime.now(co_tz)
today = now.strftime("%Y-%m-%d")
tomorrow = now + timedelta(days=1)
tomorow_day = tomorrow.strftime("%Y-%m-%d")
#date = input("Hola, registra una fecha en formato 2021-04-10: ")
#boolean = input("Ahora, escribe '0' para dia o '1' para noche")

def posting_sheets(list_input,sheet_name,first_cell):
    range_write=sheet_name+'!'+first_cell
    value_range={'values':list_input}
    write_sheets(range_write, value_range)

def post_alimento_daily(date,initial_row):
    posting_sheets(list_textos_liturgia(date),'Santifica el día','H'+str(initial_row))
    posting_sheets(one_value_oraciones_liturgia(date, 'laudes'),'Santifica el día','B'+str(initial_row))
    posting_sheets(one_value_oraciones_liturgia(date, 'lectio'),'Santifica el día','B'+str(initial_row+1))
    posting_sheets(list_gracia_dia(date),'Santifica el día','B'+str(initial_row+2))
    posting_sheets(list_lecturas_misa(date),'Santifica el día','B'+str(initial_row+3))
    posting_sheets(one_value_oraciones_liturgia(date, 'visperas'),'Santifica el día','B'+str(initial_row+4))
    posting_sheets(one_value_oraciones_liturgia(date, 'completas'),'Santifica el día','B'+str(initial_row+5))

def post_update_dates(date,initial_row):
    list_dates = [[date] for i in range(6)]
    print(list_dates)
    posting_sheets(list_dates,'Santifica el día','G'+str(initial_row))

def post_alimento_noche(date):
    post_alimento_daily(date,8)
def post_alimento_madrugada(date):
    post_alimento_daily(date,2)

#if boolean == '0':
#    post_alimento_madrugada(date)
#elif boolean =='1':
#    post_alimento_noche(date)

try:
    print("Trying...",today)
    post_alimento_madrugada(today)
    message = f"Do it for today: {today} \n"
except:
    print("Cant do it for:",today)
    post_update_dates(today, 2)
    message = f"Cant do it for today: {today} \n"
try:
    print("Trying...",tomorow_day)
    post_alimento_noche(tomorow_day)
    message += f"Do it for tomorrow: {tomorow_day} \n"
except:
    print("Cant do it for:",tomorow_day)
    post_update_dates(tomorow_day, 8)
    message += f"Cant do it for tomorrow: {tomorow_day} \n"


send_whatsapp_message(message)

#posting_sheets(list_oraciones_liturgia(date),'Santifica el día','A24')


#update_night(date,range_write):
#   update_laudes(date), update_lectio(date), update_gracia(date), update_homilia(date)
#update_morning(date,range_write):
#   update_visperas(date), update_completas(date)
