"""
Clock Project
16 Oct 2017
18 : 02
"""
import openpyxl

wb = openpyxl.load_workbook('/home/ryan/Documents/database.xlsx')
sheet = wb.active
for i in range(300):
    cell = i
    sheet.merge_cells('L{}:O{}'.format(cell,cell))
wb.save('/home/ryan/Documents/database.xlsx')
