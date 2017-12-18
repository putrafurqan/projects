import openpyxl

wb = openpyxl.load_workbook('/home/ryan/Documents/activitydata.xlsx')
sheet = wb.active
maxn = int(sheet.max_row)
row = 1
alpha_list = ["f","g"]
alpha_num = 0


for i in range(maxn):
    row += 1
    if row >= maxn:
        row = 1
        alpha_num +=1
    alphabet = alpha_list[alpha_num]
    default = sheet["h{}".format(row)].value
    sheet["h{}".format(row)] = default + "2"
    wb.save('/home/ryan/Documents/activitydata.xlsx')
