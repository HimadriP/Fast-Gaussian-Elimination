#Note : The array should have elements of the field GF(2) -- Only 0/1 
def fast_guass(arr, m_row, n_col): #m rows and n columns
    pivot = [False]*m_row
    pivot_found = False
    
    for j in range(n_col):
        pivot_found = False
        #Look for pivot
        for i in range(m_row):
            #Pivot Found at row i and column j
            if(arr[i][j] == 1):
              pivot[i] = True
              pivot_found = True
              break
          
        if (pivot_found == True):

            for k in range(n_col):
                
                #Pivot row
                if(k == j):
                    continue

                if (arr[i][k] == 1):
                    for row_index in range(m_row):
                        arr[row_index][k] += arr[row_index][j]
                        
    return (arr,pivot)

def find_dependent_rows(arr, pivot, m_row):

    for i in range(m_row):
        if pivot[i] == False:
            dependent_row = i

            
