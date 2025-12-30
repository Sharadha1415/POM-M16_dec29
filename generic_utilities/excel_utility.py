import xlrd

def read_excel(file_path, sheetname):
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    header = next(rows)
    d = {}
    for ele in rows:
        d[ele[0].value] = (ele[1].value)

    return d

path = r'C:\Users\Ramya\PycharmProjects\POM-M16-Dec26-2025\external_files\testdata.xlsx'
data = read_excel(path, 'data')
print(data)









