import os
import sys
sys.path.append(os.path.abspath('../'))
import datetime
import openpyxl


def handle_trip_expenses(column_numbers=None,column_details=None ,
                         amount_details=None,file_name=None):

    ##### File creating a excel and enter values into the cells depends on the user data and calculate the total expenses###
    
    ### column_details = {2:"test",3:"test1"} ###
    ### column_number = enter number include header ###

    wb = openpyxl.Workbook()
    wb.get_sheet_names()
    sheet = wb.active
    sheet.title = "Expenses"
    sheet_name = wb.get_sheet_by_name("Expenses")
    
    for i in range(1,column_numbers+1):
        sheet_name['A'+str(i)] = column_details[i-1]
        if i-1 == len(amount_details):

            sheet_name['B'+str(i)] = "=SUM(B2:B6)"
        else:
            sheet_name['B'+str(i)] = amount_details[i-1]
    root_path = os.path.expanduser('~').replace("\\", "/")
    wb.save(root_path + '/PycharmProjects/Task_Automation/data_house' + '/' +file_name)


if __name__ == '__main__':
    column_details = ["Expenses_For", "Trip to Delhi", "Cab fares", "Gift",
                      "Food_Expense", "Buffer", "Total"]
    amount_details = ["Expense_Amount", 20000, 35000, 3000, 4000, 5000]
    file_name = "Trip_Expenses.xlsx"
    handle_trip_expenses(7, column_details, amount_details, file_name=file_name)
