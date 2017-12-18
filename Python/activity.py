"""
Daily Activity
22 October 2017
10 : 46
"""
import openpyxl

wb = openpyxl.load_workbook('/home/ryan/Documents/activitydata.xlsx')
sheet = wb.active
def main(sheet,wb):
    search = input("Activity: ")
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    found = []
    row = 1
    col_index = 0
    max_col = int(sheet.max_row)
    while 1:
        try:
            column = '{}{}'.format(alphabet[col_index],row)
        except IndexError:
            for i in found:
                print('{} {} {}'.format(i[:i.index('/')],i[i.index('/')+1:i.index('|')],i[i.index('|')+1:]))
            main(sheet,wb)
        if column == 'exit':
            break
        table = sheet[column].value
        time = sheet['a{}'.format(row)].value
        day = sheet['{}1'.format(alphabet[col_index - 1])].value

        try:
            if search.lower() in table.lower():
                found.append(table+'/'+day+'|'+time)

        except AttributeError:
            pass

        row += 1

        if row >= max_col:
            row = 1
            col_index += 1

    main(sheet,wb)
    wb.save('/home/ryan/Documents/activitydata.xlsx')
main(sheet,wb)
