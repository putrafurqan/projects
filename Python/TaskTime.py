"""
TaskTime
28 October 2017
17 : 31
Make a structure and logic for TaskTime.java
"""
import datetime
import openpyxl

wb = openpyxl.load_workbook('/home/ryan/Documents/activitydata.xlsx')
sheet = wb.active
time = '{}|{}'.format(str(datetime.date.today().strftime("%A")),str(datetime.datetime.now())[11:16].replace(':','')).split('|')
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
row = 1
col_index = 0
index_day = ''

def main(wb,sheet,time,index_day,row,col_index,alphabet):
    while 1:
        try:
            column = '{}{}'.format(alphabet[col_index],row)
        except IndexError:
            break
        search = sheet[column].value
        if time[0] == search :
            index_day = column[0]
            search_task(wb,sheet,time,index_day,row,alphabet,col_index)
        else:
            pass
        col_index += 1

def search_task(wb,sheet,time,index_day,row,alphabet,col_index):
    while 1:
        try:
            column = '{}{}'.format(index_day,row)
            search = sheet[column].value
            search1 = search.replace(':','').split('-')
            time_list = list(range(int(search1[0]),int(search1[1]) + 1))
            if int(time[1]) in time_list:
                col_index += 1
                print('Activity for {} :\n{} {}'.format(str(datetime.datetime.now())[11:16],sheet['{}{}'.format(alphabet[col_index],
                                                        row)].value,
                                                        search))
                break
            else:
                pass

        except AttributeError:
            pass
        except ValueError:
            pass
        row += 1

main(wb,sheet,time,index_day,row,col_index,alphabet)
