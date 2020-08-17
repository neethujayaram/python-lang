import openpyxl

path="specifypath here"

wb=openpyxl.load_workbook(path)

#get all sheets
# get_sheets=wb.get_sheet_names()
# print(get_sheets)

sheet=wb.get_sheet_by_name("Sheet1")
print(sheet['A1'].value)

#or give the row and column number.
print(sheet.cell(row=1,column=1).value)