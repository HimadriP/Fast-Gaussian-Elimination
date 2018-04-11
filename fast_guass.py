#Note : The array should have elements of the field GF(2) -- Only 0/1 
def fast_guass(arr, m_row, n_col): #m rows and n columns
    pivot = [False]*m_row
    pivot_found = False
    pivot_col_to_row = {}
    
    for j in range(n_col):
        pivot_found = False
        #Look for pivot
        for i in range(m_row):
            #Pivot Found at row i and column j
            if(arr[i][j] == 1):
              pivot[i] = True
              pivot_col_to_row[j]=i
              pivot_found = True
              break
          
        if (pivot_found == True):

            for k in range(n_col):
                
                #Pivot row
                if(k == j):
                    continue

                if (arr[i][k] == 1):
                    for row_index in range(m_row):
                        arr[row_index][k] = (arr[row_index][j] + arr[row_index][k])%2
                        
    return (arr,pivot,pivot_col_to_row)

def find_dependent_rows(arr, pivot, m_row):

    for i in range(m_row):
        if pivot[i] == False:
            dependent_row = i

if __name__ == "__main__":

    with open("./testcases/input.txt") as file:
        mat = file.readlines()
        mat = [i.split() for i in mat]
        mat = [[int(t) for t in i] for i in mat]
    
    for row in mat:
        print(row)

    print ("Performing Fast Guass Elimination...")

    mat,pivot,pivot_col_to_row = fast_guass(mat,len(mat),len(mat[0]))

    for row in mat:
        print(row)
