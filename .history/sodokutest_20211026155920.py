def check_horizontal(grid, possibilities):
    
    for idx_row, row in enumerate(grid):
        for idx_col, entry in enumerate(row):
            for num in range(1,10):
                if entry == 0:
                    if num not in row:
                        print(f"adding {num} to { str((idx_row, idx_col)) }")
                        possibilities[str((idx_row, idx_col))].append(num)
    return possibilities