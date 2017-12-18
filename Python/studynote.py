"""
Accesing Excel with Python
Saturday, 23 September 2017.
17 : 38 -
"""
from date_dict import day,month
import datetime
import openpyxl

today = str(datetime.date.today()).split("-")[::-1]
wb = openpyxl.load_workbook('/home/ryan/Documents/database.xlsx')
sheet = wb.active

def add_data(sheet,wb):
    row_num = str(sheet.max_row + 1)
    time  = sheet["A" + row_num] = "{}, {} {} {}".format(day[datetime.date.today().weekday()],str(today[0]),month[int(today[1])],today[2])
    Course = sheet["D" + row_num] = str(input("Course : "))
    Learned = sheet["H" + row_num] = str(input("What I've Learned : "))
    improvement = sheet["L" + row_num] = str(input("Improvements : "))
    wb.save('/home/ryan/Documents/database.xlsx')

add_data(sheet,wb)
