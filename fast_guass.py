import argparse

#Note : The matay should have elements of the field GF(2) -- Only 0/1 
def fast_guass(mat): #m rows and n columns

    m_row = len(mat)
    n_col = len(mat[0])

    if(m_row < n_col):
        print("More Data needed, Enter more rows.")
    
    pivot = [False]*m_row
    pivot_found = False
    pivot_col_to_row = {}
    
    for j in range(n_col):
        pivot_found = False
        #Look for pivot
        for i in range(m_row):
            #Pivot Found at row i and column j
            if(mat[i][j] == 1):
              pivot[i] = True
              pivot_col_to_row[j]=i
              pivot_found = True
              break
          
        if (pivot_found == True):

            for k in range(n_col):
                
                #Pivot row
                if(k == j):
                    continue

                if (mat[i][k] == 1):
                    for row_index in range(m_row):
                        mat[row_index][k] = (mat[row_index][j] + mat[row_index][k])%2
                        
    return (mat,pivot,pivot_col_to_row)

def find_dependent_rows(mat, pivot, pivot_col_to_row):

    m_row = len(mat)
    n_col = len(mat[0])
    
    for i in range(m_row):
        #Find Dependent Rows
        if (pivot[i] == False):
            dep_row = mat[i]
            dependency = [i]
            for j,val in enumerate(dep_row):
                if (val==1):
                    dependency.append(pivot_col_to_row[j])

            dependency = [a+1 for a in dependency]
            dependency.sort()
            print("Found Dependency between rows: ",dependency)

                
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Perform Fast Guassian Elimination")
    parser.add_argument('-path', type=str, required=True)
    args = parser.parse_args()

    path = args.path
    
    with open(path) as file:
        mat = file.readlines()
        mat = [i.split() for i in mat]
        mat = [[int(t) for t in i] for i in mat]
    
    for row in mat:
        print(row)

    print ("Performing Fast Guass Elimination... *s represent pivot rows")

    mat,pivot,pivot_col_to_row = fast_guass(mat)

    for i,row in enumerate(mat):

        if (pivot[i]):
            print(row," *")
            continue

        print(row)
        

    find_dependent_rows(mat,pivot,pivot_col_to_row)

    
