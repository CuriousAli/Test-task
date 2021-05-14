from openpyxl import *


# define source
def get_xl_values():
    wb = load_workbook('./media/Models_data.xlsx')
    sheet = wb.get_sheet_by_name('Models data')

    #read and return values from excel table
    values_of_rows = []
    detail = []
    counter = 0
    for cell_obj in sheet['A1':'D7']:
        for cell in cell_obj:
            if cell.value == None:
                cell.value = '-'
            counter += 1
            detail.append(cell.value)
            if counter % 4 == 0:
                values_of_rows.append(detail)
                detail = []

    return values_of_rows
