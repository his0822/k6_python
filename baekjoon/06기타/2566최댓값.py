max_val = 0
max_pos = (0,0)
for i, rows in enumerate(data, start=1):
    for j, row in enumerate(rows, start =1):
        if max_val < row:
            