def print_matrix(matrix):
    for i in matrix:  # outer loop  
            for j in i:  # inner loop               
                print(f'[{j.row}][{j.col}] {j.time_taken}', end = " ") # print the elements  
            print()