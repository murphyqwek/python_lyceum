import xlrd
rb = xlrd.open_workbook('9.xls',formatting_info=True)

res = 0

sheet = rb.sheet_by_index(0)

def get_repited_num(row):
    row = sorted(row)
    for j in range(0, 5):
        if row[j] == row[j+1]:
            return row[j]

for i in range(0, 6400):
    row = list(map(int, sheet.row_values(i)))

    len_set = len(set(row))
    
    if len_set + 1 == 6:
        repited_num = get_repited_num(row)
        set_ = set(row)
        set_.remove(repited_num)
        if repited_num*2 >= sum(set_)/4:
            res += 1

print(res)
        
